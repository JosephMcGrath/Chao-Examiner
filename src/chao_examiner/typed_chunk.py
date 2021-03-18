"""
Utilities to unpack chunks as their appropriate Python type.
"""
import struct
from typing import Any, Dict

from .binary_loader import BinaryChunk
from .chao_data import CHARACTER_ENCODING

# TODO : Validate and throw warnings using the chunk's label.


class TypedChunk(BinaryChunk):
    """
    A chunk of binary data representing a known data type.
    """

    type_label = "Not a type"
    format = "B"

    def __init__(
        self, label: str, data: bytes, start: int, lookup: Dict[int, str]
    ) -> None:
        super().__init__(
            label=label,
            data=data,
            start=start,
            end=start + struct.calcsize(self.format),
        )
        self.lookup = lookup

    def get_value(self) -> int:
        """
        Extract the value of the byte.
        """
        return struct.unpack(self.format, self.data)[0]

    def set_value(self, value: int) -> None:
        """
        Set the value of the byte.
        """
        self.data = struct.pack(self.format, value)


class ByteChunk(TypedChunk):
    """
    A chunk holding an integer in a single byte.
    """

    type_label = "Byte"
    format = "B"


class SignedByteChunk(TypedChunk):
    """
    A chunk holding an integer in a single signed byte.
    """

    type_label = "Signed byte"
    format = "b"


class ShortChunk(TypedChunk):
    """
    A chunk holding a short integer number in 2 bytes.
    """

    type_label = "Short"
    format = "H"


class IntChunk(TypedChunk):
    """
    A chunk holding an integer number in 4 bytes.
    """

    type_label = "Int"
    format = "I"


class FloatChunk(TypedChunk):
    """
    A chunk holding a floating point number in 4 bytes.
    """

    type_label = "Float"
    format = "f"


class BooleanChunk(TypedChunk):
    """
    A chunk holding a boolean value in a single byte.
    """

    type_label = "Boolean"
    format = "?"


class ChaoNameChunk(TypedChunk):
    """
    A chunk holding a chao's name.

    This is a special case spanning 7 bytes.
    """

    type_label = "Name"
    format = "BBBBBBB"

    def get_value(self) -> str:
        """
        Extract the value of the byte.
        """
        return "".join([CHARACTER_ENCODING[int(x)] for x in self.data])

    def set_value(self, value: str) -> None:
        """
        Set the value of the byte.
        """
        # TODO encode characters.
        self.data = bytes(value)


class TimeChunk(TypedChunk):
    """
    A chunk holding a Sonic Adventure time.

    This is stored in 3 bytes, minutes, seconds & milliseconds.
    """

    type_label = "Time"
    format = "BBB"

    def get_value(self) -> str:
        """
        Extract the value of the byte.
        """
        # TODO : Something's up with milliseconds.
        return ":".join([f"{int(x):02}" for x in self.data])

    def set_value(self, value: str) -> None:
        """
        Set the value of the byte.
        """
        # TODO encode times.
        self.data = bytes(value)


class ByteLookup(ByteChunk):
    """
    A chunk holding a lookup value in a single byte.
    """

    type_label = "ByteLookup"

    def get_value(self) -> int:
        """
        Extract the value of the byte.
        """
        value = struct.unpack(self.format, self.data)[0]
        if value not in self.lookup:
            raise KeyError(
                f"{self.label} lookup table doesn't have a value for '{value}'."
            )
        return self.lookup[value]

    def set_value(self, value: int) -> None:
        """
        Set the value of the byte.
        """
        number = [x for x, y in self.lookup.items() if y == value]
        self.data = struct.pack(self.format, number)


class IntFlags(IntChunk):
    """
    A series of boolean flags stored in a 4-byte sequence.
    """

    type_label = "IntFlags"

    flag_keys = [2 ** x for x in range(31, -1, -1)]

    def get_value(self) -> int:
        """
        Extract the value of the byte.
        """
        output = {}
        value = struct.unpack(self.format, self.data)[0]
        for key in self.flag_keys:
            if key not in self.lookup:
                continue
            output[self.lookup[key]] = key <= value
            if key <= value:
                value -= key

        return output

    # TODO : Reverse operation.


class ShortFlags(ShortChunk):
    """
    A series of boolean flags stored in a 2-byte sequence.
    """

    type_label = "ShortFlags"

    flag_keys = [2 ** x for x in range(15, -1, -1)]

    def get_value(self) -> int:
        """
        Extract the value of the byte.
        """
        output = {}
        value = struct.unpack(self.format, self.data)[0]
        for key in self.flag_keys:
            if key not in self.lookup:
                continue
            output[self.lookup[key]] = key <= value
            if key <= value:
                value -= key

        return output

    # TODO : Reverse operation.


CHUNK_TYPES = [
    ByteChunk,
    SignedByteChunk,
    ShortChunk,
    IntChunk,
    FloatChunk,
    BooleanChunk,
    ChaoNameChunk,
    TimeChunk,
    ByteLookup,
    ShortFlags,
    IntFlags,
]
CHUNK_LOOKUP = {x.type_label: x for x in CHUNK_TYPES}

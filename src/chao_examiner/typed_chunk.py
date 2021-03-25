"""
Utilities to unpack chunks as their appropriate Python type.
"""
import struct
from typing import Any, Dict, List, Optional

from .binary_loader import BinaryChunk
from .chao_data import CHARACTER_ENCODING


class TypedChunk(BinaryChunk):
    """
    A chunk of binary data representing a known data type.
    """

    type_label = "Not a type"
    format = "B"

    @classmethod
    def load(
        cls,
        label: str,
        data: bytes,
        start: int,
        lookup: Optional[Dict[int, str]] = None,
        group: Optional[str] = None,
    ) -> "TypedChunk":
        """
        Load the chunk based on it's typed properties.
        """
        output = cls(
            label=label,
            data=data,
            start=start,
            end=start + struct.calcsize(cls.format),
        )
        if lookup is None:
            output.lookup = {}
        else:
            output.lookup = lookup
        output.group = group
        return output

    def __init__(self, label: str, data: bytes, start: int, end: int) -> None:
        super().__init__(
            label=label,
            data=data,
            start=start,
            end=end,
        )
        self.lookup: Dict[int, str]
        self.group: Optional[str]

    def get_value(self) -> Any:
        """
        Extract the value of the byte.
        """
        return struct.unpack(self.format, self.data)[0]

    def set_value(self, value: Any) -> None:
        """
        Set the value of the byte.
        """
        self.update(struct.pack(self.format, value))


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

        if not isinstance(value, str):
            raise TypeError(f"Chao name has to be a string, not {type(value)}")
        if len(value) > 7:
            raise ValueError(
                f"Chao name must be at most 7 characters, not {len(value)}"
            )

        accumulator: List[int] = []
        for character in range(7):
            if character > len(value) - 1:
                accumulator.append(0)
                continue
            accumulator.extend(
                [x for x, y in CHARACTER_ENCODING.items() if y == value[character]]
            )
        self.update(bytes(accumulator))


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
        return ":".join([f"{int(x):02}" for x in self.data])

    def set_value(self, value: str) -> None:
        """
        Set the value of the byte.
        """
        parts = value.split(":")
        if len(parts) != 3:
            raise ValueError("Number must be formatted minutes:seconds:milliseconds.")
        if any(not x.isnumeric() for x in parts):
            raise ValueError("Each part of the time must be a number.")

        self.update(bytes([int(x) for x in parts]))


class ByteLookup(ByteChunk):
    """
    A chunk holding a lookup value in a single byte.
    """

    type_label = "ByteLookup"

    def get_value(self) -> str:
        """
        Extract the value of the byte.
        """
        value = struct.unpack(self.format, self.data)[0]
        if value not in self.lookup:
            raise KeyError(
                f"{self.label} lookup table doesn't have a value for '{value}'."
            )
        return self.lookup[value]

    def set_value(self, value: str) -> None:
        """
        Set the value of the byte.
        """
        if value not in self.lookup.values():
            raise KeyError(f"{value} isn't a valid lookup value.")
        number = [x for x, y in self.lookup.items() if y == value][0]
        self.update(struct.pack(self.format, number))


class IntFlags(IntChunk):
    """
    A series of boolean flags stored in a 4-byte sequence.
    """

    type_label = "IntFlags"

    flag_keys = [2 ** x for x in range(31, -1, -1)]

    def get_value(self) -> Dict[str, bool]:
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

    def set_value(self, value: Dict[str, bool]) -> None:
        """
        Set the value of the byte.
        """
        inverted_lookup = {y: x for x, y in self.lookup.items()}
        to_set = 0
        for new_key, new_value in value.items():
            if new_key not in inverted_lookup:
                raise ValueError(f"{new_key} not in lookup table {inverted_lookup}.")
            if new_value:
                to_set += inverted_lookup[new_key]
        self.update(struct.pack(self.format, to_set))


class ShortFlags(IntFlags):
    """
    A series of boolean flags stored in a 2-byte sequence.
    """

    type_label = "ShortFlags"
    format = "H"


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

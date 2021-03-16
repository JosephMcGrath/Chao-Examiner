"""
Utilities to unpack chunks as their appropriate Python type.
"""
import struct
from typing import Any

from .binary_loader import BinaryChunk

# TODO : Validate and throw warnings using the chunk's label.


class TypedChunk(BinaryChunk):
    """
    A chunk of binary data representing a known data type.
    """

    label = "Not a type"
    format = "B"

    def __init__(self, label: str, data: bytes, start: int) -> None:
        super().__init__(
            label=label,
            data=data,
            start=start,
            end=start + struct.calcsize(self.format),
        )

    def get_value(self) -> Any:
        """
        Interpret the binary data as its proper type.
        """
        raise NotImplementedError("Not implemented by the base class.")

    def set_value(self, value: Any) -> None:
        """
        Set the binary data from its proper type.
        """
        raise NotImplementedError("Not implemented by the base class.")


class ByteChunk(TypedChunk):
    """
    A chunk holding an integer in a single byte.
    """

    label = "Byte"
    format = "B"

    def get_value(self) -> int:
        """
        Extract the value of the byte.
        """
        return [int(x) for x in self.data][0]

    def set_value(self, value: int) -> None:
        """
        Set the value of the byte.
        """
        self.data = bytes([value])


class SignedByteChunk(TypedChunk):
    """
    A chunk holding an integer in a single signed byte.
    """

    label = "Signed byte"
    format = "b"

    def get_value(self) -> int:
        """
        Extract the value of the byte.
        """
        return [int(x) for x in self.data][0]

    def set_value(self, value: int) -> None:
        """
        Set the value of the byte.
        """
        self.data = bytes([value])


class ShortChunk(TypedChunk):
    """
    A chunk holding a short integer number in 2 bytes.
    """

    label = "Short"
    format = "H"

    def get_value(self) -> int:
        """
        Extract the value of the byte.
        """
        return [int(x) for x in self.data][0]

    def set_value(self, value: int) -> None:
        """
        Set the value of the byte.
        """
        self.data = bytes([value])


class IntChunk(TypedChunk):
    """
    A chunk holding an integer number in 4 bytes.
    """

    label = "Int"
    format = "I"

    def get_value(self) -> int:
        """
        Extract the value of the byte.
        """
        return [int(x) for x in self.data][0]

    def set_value(self, value: int) -> None:
        """
        Set the value of the byte.
        """
        self.data = bytes([value])


class FloatChunk(TypedChunk):
    """
    A chunk holding a floating point number in 4 bytes.
    """

    label = "Float"
    format = "f"

    def get_value(self) -> int:
        """
        Extract the value of the byte.
        """
        return [int(x) for x in self.data][0]

    def set_value(self, value: int) -> None:
        """
        Set the value of the byte.
        """
        self.data = bytes([value])


class BooleanChunk(TypedChunk):
    """
    A chunk holding a boolean value in a single byte.
    """

    label = "Boolean"
    format = "?"

    def get_value(self) -> int:
        """
        Extract the value of the byte.
        """
        return [int(x) for x in self.data][0]

    def set_value(self, value: int) -> None:
        """
        Set the value of the byte.
        """
        self.data = bytes([value])


CHUNK_TYPES = [
    ByteChunk,
    SignedByteChunk,
    ShortChunk,
    IntChunk,
    FloatChunk,
    BooleanChunk,
]
CHUNK_LOOKUP = {x.label: x for x in CHUNK_TYPES}

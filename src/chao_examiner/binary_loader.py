"""
Load / save raw binary data.
"""

import logging
from typing import Dict, Optional, Union

from .logs import LOG_NAME


class BinaryChunk:
    """
    A sub-division of a larger bytes object to facilitate updating sections.
    """

    def __init__(self, label: str, data: bytes, start: int, end: int) -> None:
        self.label = label
        self.data = data[start:end]
        self.start = start
        self.end = end

    def inject(self, target_data: Union["BinaryLoader", bytes]) -> bytes:
        """
        Inject the chunk into a bytes object at it's correct place.

        If the target is a BinaryLoader, the data is also updated.
        """
        if isinstance(target_data, BinaryLoader):
            binary = target_data.binary
        elif isinstance(target_data, bytes):
            binary = target_data
        else:
            raise TypeError("Can only inject data into a Bytes of BinaryLoader")

        binary = binary[: self.start] + self.data + binary[self.end :]

        if isinstance(target_data, BinaryLoader):
            target_data.binary = binary

        return binary

    def update(self, new_data: bytes) -> None:
        """Replace the data with a new bytes object (with checks)."""
        if not isinstance(new_data, bytes):
            raise TypeError("Can only update with a bytes object.")
        if len(new_data) != len(self.data):
            raise ValueError(
                f"Binary data is the wrong size ({len(new_data)}) rather than ({len(self.data)})"
            )
        self.data = new_data

    def clear(self) -> None:
        """Wipe the data from the chunk."""
        self.data = b"\x00" * (self.end - self.start)

    def swap(self, new_data: bytes, target_data: Union["BinaryLoader", bytes]) -> bytes:
        """Update the chunk to the new data and inject it into the larget binary."""
        self.update(new_data)
        return self.inject(target_data)

    def __str__(self) -> str:
        return f"<BinaryChunk {self.label} ({len(self.data)} bytes, start={self.start}, end={self.end})>"

    __repr__ = __str__

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BinaryChunk):
            raise TypeError("Can only compare a BinaryChunk to another BinaryChunk.")
        if self.label != other.label:
            return False
        if self.data != other.data:
            return False
        if self.start != other.start:
            return False
        if self.end != other.end:
            return False
        return True


class BinaryLoader:
    """
    Manages loading, saving and splitting up binary data.
    """

    def __init__(self, binary_data: bytes) -> None:
        self.binary = binary_data
        self.chunks: Dict[str, BinaryChunk] = {}

    @classmethod
    def _log(cls, name: Optional[str] = None) -> logging.Logger:
        if name is None:
            return logging.getLogger(LOG_NAME + ".BinaryLoader")
        return logging.getLogger(LOG_NAME + f".BinaryLoader.{name}")

    @classmethod
    def read(cls, file_path: str) -> "BinaryLoader":
        """Read chao data from a binary file."""
        logger = cls._log()
        logger.info("Loading binary data from %s.", file_path)
        with open(file_path, "rb") as file:
            data = file.read()
        output = cls(data)
        logger.info("Finished loading binary data from %s.", file_path)
        return output

    def write(self, file_path: str) -> None:
        """Write chao data to a binary file."""
        logger = self._log()
        logger.info("Saving binary data to %s.", file_path)
        with open(file_path, "wb") as file:
            file.write(self.binary)
        logger.info("Finished saving binary data to %s.", file_path)

    def chunk(self, label: str, start: int, end: int) -> BinaryChunk:
        """Create a labelled chunk of data."""
        self._log("Chunk").debug(
            "Creating binary chunk named '%s' from %s to %s.", label, start, end
        )
        self.chunks[label] = BinaryChunk(label, self.binary, start, end)
        return self.chunks[label]

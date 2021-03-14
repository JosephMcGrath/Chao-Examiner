"""
Load / save raw binary data.
"""

import logging
from typing import Optional

from .logs import LOG_NAME


class BinaryLoader:
    """
    Manages loading, saving and splitting up binary data.
    """

    def __init__(self, binary_data: bytes) -> None:
        self.binary = binary_data

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

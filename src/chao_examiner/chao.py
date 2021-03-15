import logging
from typing import Optional

from .binary_loader import BinaryLoader
from .logs import LOG_NAME


class Chao:
    def __init__(self, binary: bytes) -> None:
        self.binary = binary

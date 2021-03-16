"""
Data defining an individual chao.
"""

import logging
from typing import Optional, List

from .binary_loader import BinaryChunk
from .logs import LOG_NAME

from .chao_offsets import CHAO_OFFSETS, DATA_TYPE_LENGTHS


class Chao:
    """
    A chao.
    """

    def __init__(self, binary: bytes) -> None:
        self.binary = binary
        self.chunks: List[BinaryChunk] = []

        self._create_chunks()

    def _create_chunks(self) -> None:
        for label, details in CHAO_OFFSETS.items():
            self.chunks.append(
                BinaryChunk(
                    label=label,
                    data=self.binary,
                    start=details["offset"],
                    end=details["offset"] + DATA_TYPE_LENGTHS[details["data_type"]],
                )
            )

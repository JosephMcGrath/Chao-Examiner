"""
Utilities to manage a single Sonic Adventure 2 Battle (steam) chao save file.
"""


import logging
from typing import Optional, List

from .binary_loader import BinaryLoader, BinaryChunk
from .chao import Chao
from .logs import LOG_NAME


class ChaoSaveFile:
    """
    A single Sonic Adventure 2 Battle (steam) chao save file.
    """

    data_start = 15012
    data_length = 2047
    data_count = 24

    def __init__(self, path: str) -> None:
        self.path = path
        self.loader = BinaryLoader.read(path)
        self.chao: List[BinaryChunk] = []

        required_length = self.data_start + (self.data_length * self.data_count)
        if len(self.loader.binary) < required_length:
            raise ValueError(
                f"Data is too short ({len(self.loader.binary)} vs {required_length}"
            )

        start_byte = self.data_start
        for chao_no in range(self.data_count):
            end_byte = start_byte + self.data_length
            chao_name = f"chao_{chao_no + 1}"
            self.chao.append(self.loader.chunk(chao_name, start_byte, end_byte))
            start_byte = end_byte + 1

    def write(self, path: Optional[str] = None) -> None:
        """Write the save file to its original or the selected path."""
        # TODO : Not currently writing valid saves.
        if path is None:
            path = self.path
        self.loader.write(path)

    @classmethod
    def _log(cls, name: Optional[str] = None) -> logging.Logger:
        if name is None:
            return logging.getLogger(LOG_NAME + ".SaveFile")
        return logging.getLogger(LOG_NAME + f".SaveFile.{name}")

    def get_chao(self, chao_no: int) -> Chao:
        """
        Get the Chao at a numbered slot.
        """
        logger = self._log()
        logger.debug("Getting chao %s.", chao_no)
        if chao_no > len(self.chao) or chao_no < 0:
            raise KeyError(
                f"No chao with an index of {chao_no}, please enter a value between 0 and {len(self.chao)}"
            )

        chao_chunk = self.chao[chao_no]
        return Chao(chao_chunk.data)

    def set_chao(self, chao: Chao, chao_no: int) -> None:
        """
        Update the numbered slot to be the provided Chao.
        """
        logger = self._log()
        logger.debug("Setting chao %s.", chao_no)
        self.chao[chao_no].swap(chao.binary, self.loader)

    def clear_chao(self, chao_no: int) -> None:
        """
        Clear the save slot for a numbered Chao.
        """
        logger = self._log()
        logger.debug("Clearing chao %s.", chao_no)
        self.chao[chao_no].clear()
        self.chao[chao_no].inject(self.loader)

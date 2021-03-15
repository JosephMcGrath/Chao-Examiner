import logging
from typing import Optional, List

from .binary_loader import BinaryLoader, BinaryChunk
from .chao import Chao
from .logs import LOG_NAME


class SaveFile:

    data_start = 15012
    data_length = 2048
    data_count = 24

    def __init__(self, path: str) -> None:
        self.loader = BinaryLoader.read(path)
        self.chao: List[BinaryChunk] = []
        # TODO : Check length
        for chao_no, line_no in enumerate(
            [self.data_start + x * self.data_length for x in range(self.data_count)]
        ):
            chao_name = f"chao_{chao_no + 1}"
            self.chao.append(
                self.loader.chunk(chao_name, line_no, line_no + self.data_length)
            )

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
        # TODO : BinaryChunk wants a single-operation "swap" method.
        logger = self._log()
        logger.debug("Setting chao %s.", chao_no)
        self.chao[chao_no].update(chao.binary)
        self.chao[chao_no].inject(self.loader)

    def clear_chao(self, chao_no: int) -> None:
        """
        Clear the save slot for a numbered Chao.
        """
        logger = self._log()
        logger.debug("Clearing chao %s.", chao_no)
        self.chao[chao_no].clear()
        self.chao[chao_no].inject(self.loader)

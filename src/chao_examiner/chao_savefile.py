"""
Utilities to manage a single Sonic Adventure 2 Battle (steam) chao save file.
"""


import glob
import json
import logging
import os
from typing import Dict, List, Optional

from .binary_loader import BinaryChunk, BinaryLoader
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

    @classmethod
    def find(cls, path: str) -> "ChaoSaveFile":
        """
        Find the save file from the starting path provided.
        """
        if os.path.split(path)[1] == "SONIC2B__ALF":
            return cls(path)

        candidates = glob.glob(f"{path}/**/SONIC2B__ALF", recursive=True)
        if len(candidates) == 0:
            raise FileNotFoundError("No Chao savefile found at that path.")
        if len(candidates) > 1:
            raise RuntimeError("More than one Chao savefile found at that path.")

        return cls(candidates[0])

    def write(self, path: Optional[str] = None) -> None:
        """Write the save file to its original or the selected path."""
        if path is None:
            path = self.path
        self.loader.write(path)

    def to_json(self, path: str) -> None:
        """Write all the chao in the file to JSON."""
        for chao_no in range(24):
            chao = self.get_chao(chao_no)
            if not chao.is_active():
                continue
            output_path = os.path.join(path, f"chao_{str(chao_no).zfill(2)}.json")
            chao.to_json(output_path)

    def unresolved_bytes(self) -> Dict[int, int]:
        """
        Create a dictionary describing un-resolved bytes in the savefile, listed by byte
        offset.
        """
        resolved: List[int] = []
        for chao in self.chao:
            resolved.extend(range(chao.start, chao.end))
        return {
            x: int(y) for x, y in enumerate(self.loader.binary) if x not in resolved
        }

    def unresolved_json(self, path: str) -> None:
        """
        Export all un-resolved bytes to JSON.
        """
        with open(path, "w", encoding="utf-8") as file:
            json.dump(self.unresolved_bytes(), file, indent=4)

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


# TODO non-chao data.

"""
Data defining an individual chao.
"""

import json
import logging
from typing import Any, Dict, List, Optional

from .chao_data import CHAO_OFFSETS, LOOKUP_TABLES
from .logs import LOG_NAME
from .typed_chunk import CHUNK_LOOKUP, TypedChunk


class Chao:
    """
    A chao.
    """

    def __init__(self, binary: bytes) -> None:
        self.binary = binary
        self.chunks: List[TypedChunk] = []

        self._create_chunks()

    @classmethod
    def _log(cls, name: Optional[str] = None) -> logging.Logger:
        if name is None:
            return logging.getLogger(LOG_NAME + ".Chao")
        return logging.getLogger(LOG_NAME + f".Chao.{name}")

    def is_active(self) -> bool:
        """Check if the Chao is active."""
        return bool(sum(self.binary))

    def _create_chunks(self) -> None:
        for chunk in CHAO_OFFSETS:
            if chunk["Data type"] not in CHUNK_LOOKUP:
                self._log().warning(
                    "Couldn't read chunk %s - data type = %s.",
                    chunk["Attribute"],
                    chunk["Data type"],
                )
                continue
            offset = chunk["Offset"]
            if not isinstance(offset, int):
                raise TypeError(
                    f"{chunk['Attribute']}.Offset is the wrong type ({type(chunk['Offset'])})"
                )

            data_loader = CHUNK_LOOKUP[str(chunk["Data type"])]
            lookup = LOOKUP_TABLES.get(str(chunk["Lookup"]), {})

            self.chunks.append(
                data_loader.load(
                    label=str(chunk["Attribute"]),
                    data=self.binary,
                    start=offset,
                    lookup=lookup,
                    group=chunk.get("Group"),
                )
            )

    def unresolved_bytes(self) -> Dict[int, int]:
        """
        Create a dictionary describing un-resolved bytes in the chao, listed by byte
        offset.
        """
        resolved: List[int] = []
        for chunk in self.chunks:
            resolved.extend(range(chunk.start, chunk.end))
        return {x: int(y) for x, y in enumerate(self.binary) if x not in resolved}

    def _unresolved_bytes_str(self) -> Dict[int, str]:

        resolved: List[int] = []
        for chunk in self.chunks:
            resolved.extend(range(chunk.start, chunk.end))

        output = {}
        accumulator = ""
        starts_at = -1
        for offset, byte_value in enumerate(self.binary):
            if offset in resolved:
                if accumulator:
                    output[starts_at] = accumulator
                    accumulator = ""
                    starts_at = -1
                continue
            if starts_at == -1:
                starts_at = offset
            accumulator += "|" + str(int(byte_value))
        output[starts_at] = accumulator

        return output

    def to_dict(self) -> Dict[str, int]:
        """
        Export the Chao to a dictionary.
        """
        output = {}
        for attribute in self.chunks:
            if attribute.group is None:
                output[attribute.label] = attribute.get_value()
            else:
                if attribute.group in output:
                    output[attribute.group][attribute.label] = attribute.get_value()
                else:
                    output[attribute.group] = {attribute.label: attribute.get_value()}

        output["unresolved"] = self._unresolved_bytes_str()
        return output

    def to_json(self, path: str) -> None:
        """
        Export the Chao to a JSON file.
        """
        with open(path, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, indent=4)

    def __str__(self) -> str:
        return f"<Chao: {self['Name']}>"

    __repr__ = __str__

    def __getitem__(self, label: str) -> TypedChunk:
        candidates = [chunk for chunk in self.chunks if chunk.label == label]
        if len(candidates) == 0:
            raise KeyError(f"Chao has no label: {label}.")
        if len(candidates) > 1:
            first_entry = candidates[0]
            for entry in candidates[1:]:
                if entry != first_entry:
                    self._log().warning("Inconsistent value for %s.", first_entry.label)
        return candidates[0].get_value()

    def __setitem__(self, label: str, value: Any) -> None:

        for chunk in self.chunks:
            if chunk.label != label:
                continue
            chunk.set_value(value)
            self.binary = chunk.inject(self.binary)

"""
Data defining an individual chao.
"""

import logging
from typing import Dict, List, Optional
import json
from .chao_data import CHAO_OFFSETS, DATA_TYPE_LENGTHS
from .logs import LOG_NAME
from .typed_chunk import CHUNK_LOOKUP, TypedChunk


class Chao:
    """
    A chao.
    """

    def __init__(self, binary: bytes) -> None:
        self.binary = binary
        self.chunks: Dict[str, TypedChunk] = {}

        self._create_chunks()

    def _create_chunks(self) -> None:
        for chunk in CHAO_OFFSETS:
            if chunk["Data type"] not in CHUNK_LOOKUP:
                print(
                    f"Couldn't read chunk {chunk['Attribute']} - data type = {chunk['Data type']}"
                )
                continue

            data_loader = CHUNK_LOOKUP[chunk["Data type"]]

            self.chunks[chunk["Attribute"]] = data_loader(
                label=chunk["Attribute"],
                data=self.binary,
                start=chunk["Offset"],
            )
        
    def _unresolved_bytes(self) -> Dict[str, int]:
        resolved = []
        for chunk in self.chunks.values():
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
        for attribute in self.chunks.values():
            output[attribute.label] = attribute.get_value()
        output["unresolved"] = self._unresolved_bytes()
        return output

    def to_json(self, path: str) -> None:
        """
        Export the Chao to a JSON file.
        """
        with open(path, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, indent=4)

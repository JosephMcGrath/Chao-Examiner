"""
Data defining an individual chao.
"""

from typing import Any, Dict, List
import json
from .chao_data import CHAO_OFFSETS, LOOKUP_TABLES
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
                # TODO : Logger.warning
                print(
                    f"Couldn't read chunk {chunk['Attribute']} - data type = {chunk['Data type']}"
                )
                continue
            offset = chunk["Offset"]
            if not isinstance(offset, int):
                raise TypeError(
                    f"{chunk['Attribute']}.Offset is the wrong type ({type(chunk['Offset'])})"
                )

            data_loader = CHUNK_LOOKUP[str(chunk["Data type"])]
            lookup = LOOKUP_TABLES.get(str(chunk["Lookup"]), {})

            self.chunks[str(chunk["Attribute"])] = data_loader.load(
                label=str(chunk["Attribute"]),
                data=self.binary,
                start=offset,
                lookup=lookup,
            )

    def unresolved_bytes(self) -> Dict[int, int]:
        """
        Create a dictionary describing un-resolved bytes in the chao, listed by byte
        offset.
        """
        resolved: List[int] = []
        for chunk in self.chunks.values():
            resolved.extend(range(chunk.start, chunk.end))
        return {x: int(y) for x, y in enumerate(self.binary) if x not in resolved}

    def _unresolved_bytes_str(self) -> Dict[int, str]:

        resolved: List[int] = []
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
        output["unresolved"] = self._unresolved_bytes_str()
        return output

    def to_json(self, path: str) -> None:
        """
        Export the Chao to a JSON file.
        """
        with open(path, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, indent=4)

    def __getitem__(self, label: str) -> TypedChunk:
        return self.chunks[label].get_value()

    def __setitem__(self, label: str, value: Any) -> None:
        chunk: TypedChunk = self.chunks[label]
        chunk.set_value(value)
        self.binary = chunk.inject(self.binary)

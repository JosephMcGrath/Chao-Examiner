# # pylint: disable=too-few-public-methods
"""
Shared functionality mixin to support shared data chunking behaviour.
"""

import logging
from typing import Any, Dict, List, Optional, Union

from .chao_data import LOOKUP_TABLES
from .logs import LOG_NAME
from .typed_chunk import CHUNK_LOOKUP, TypedChunk

MYPY = False


class ChunkExtractor:
    """
    Mixin to support shared functionality between
    """

    offsets: List[Dict[str, Union[str, int, None]]]

    if MYPY:
        # Doing this to keep MyPy happy.
        binary: bytes
        chunks: List[TypedChunk] = []

    @classmethod
    def _log(cls, name: Optional[str] = None) -> logging.Logger:
        if name is None:
            return logging.getLogger(LOG_NAME)
        return logging.getLogger(f"{LOG_NAME}.{name}")

    def _create_chunks(self) -> None:
        for chunk in self.offsets:
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
            if chunk.get("Group") is None:
                group_name: Optional[str] = None
            else:
                group_name = str(chunk.get("Group"))

            self.chunks.append(
                data_loader.load(
                    label=str(chunk["Attribute"]),
                    data=self.binary,
                    start=offset,
                    lookup=lookup,
                    group=group_name,
                )
            )

    def to_dict(self) -> Dict[str, Any]:
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

        return output

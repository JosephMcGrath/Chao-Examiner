"""
Checks on the data used to load data from the chao save-file.
"""

from chao_examiner.chao_data import CHAO_OFFSETS, LOOKUP_TABLES
from chao_examiner.typed_chunk import CHUNK_LOOKUP


def test_schema():
    """
    Check that all offsets use the correct format.
    """
    for this_offset in CHAO_OFFSETS:
        print(this_offset)
        assert len(this_offset) == 4
        assert isinstance(this_offset["Attribute"], str)
        assert isinstance(this_offset["Offset"], int)
        assert isinstance(this_offset["Data type"], str)
        assert isinstance(this_offset["Lookup"], str) or this_offset["Lookup"] is None
        assert this_offset["Data type"] in CHUNK_LOOKUP


def test_lookups():
    """
    Check that all lookups exist and that all lookups are used.
    """
    lookups = {x for x in LOOKUP_TABLES}
    for this_offset in CHAO_OFFSETS:
        if this_offset["Lookup"] is None:
            continue
        assert this_offset["Lookup"] in lookups

    lookups_used = {x["Lookup"] for x in CHAO_OFFSETS if x["Lookup"] is not None}
    for this_lookup in LOOKUP_TABLES:
        assert this_lookup in lookups_used


def test_order():
    """
    Check that all lookups are in the correct order.
    """
    previous = -1
    for this_offset in CHAO_OFFSETS:
        print(this_offset)
        assert this_offset["Offset"] > previous
        previous = this_offset["Offset"]

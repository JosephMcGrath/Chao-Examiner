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
        assert len(this_offset) == 5
        assert isinstance(this_offset["Attribute"], str)
        assert isinstance(this_offset["Group"], str) or this_offset["Group"] is None
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


def test_group_integrity():
    """
    Check that groups are consistent.

    If an offset occurs multiple times, all should have the same group and each group
    should have more than one entry.
    """
    offset_groups = {}
    group_counts = {}
    for this_offset in CHAO_OFFSETS:
        print(this_offset)
        if this_offset["Attribute"] not in offset_groups:
            offset_groups[this_offset["Attribute"]] = this_offset["Group"]
        assert offset_groups[this_offset["Attribute"]] == this_offset["Group"]

        if this_offset["Group"] is None:
            continue
        if this_offset["Group"] not in group_counts:
            group_counts[this_offset["Group"]] = []
        group_counts[this_offset["Group"]].append(this_offset)

    for this_group in group_counts.values():
        print(this_group)
        assert len(this_group) > 1


def test_overlaps():
    """
    Check that there's no overlaps between different chunks.
    """
    chunk_map = {}
    for chunk in CHAO_OFFSETS:
        data_loader = CHUNK_LOOKUP[str(chunk["Data type"])]
        lookup = LOOKUP_TABLES.get(str(chunk["Lookup"]), {})
        temp = data_loader.load(
            label=str(chunk["Attribute"]),
            data=b"0000000000000000000000000000",
            start=chunk["Offset"],
            lookup=lookup,
            group=chunk.get("Group"),
        )
        for n in range(temp.start, temp.end):
            print(temp.label, chunk_map)
            assert n not in chunk_map
            chunk_map[n] = temp.label

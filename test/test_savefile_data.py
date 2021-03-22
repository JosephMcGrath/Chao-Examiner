"""
Checks on the data used to load data from the save-file.
"""

from chao_examiner.save_file_data import SAVE_FILE_OFFSETS
from chao_examiner.typed_chunk import CHUNK_LOOKUP


def test_schema():
    """
    Check that all offsets use the correct format.
    """
    for this_offset in SAVE_FILE_OFFSETS:
        print(this_offset)
        assert len(this_offset) == 4
        assert isinstance(this_offset["Attribute"], str)
        assert isinstance(this_offset["Offset"], int)
        assert isinstance(this_offset["Data type"], str)
        assert isinstance(this_offset["Lookup"], str) or this_offset["Lookup"] is None
        assert this_offset["Data type"] in CHUNK_LOOKUP


def test_order():
    """
    Check that all lookups are in the correct order.
    """
    previous = -1
    for this_offset in SAVE_FILE_OFFSETS:
        print(this_offset)
        assert this_offset["Offset"] > previous
        previous = this_offset["Offset"]

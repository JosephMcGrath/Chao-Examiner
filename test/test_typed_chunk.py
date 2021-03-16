"""
Tests on loading chunks of binary data into usable data.
"""
import chao_examiner
import pytest


def test_interface_errors():
    """
    Check that NotImplementedError is raised for the interface.
    """
    data = chao_examiner.typed_chunk.TypedChunk("test", b"\x05", 0)

    with pytest.raises(NotImplementedError):
        data.get_value()

    with pytest.raises(NotImplementedError):
        data.set_value(12)


def test_byte_read():
    """
    Check that reading a byte works as intended.
    """

    data = chao_examiner.ByteChunk("test", b"\x05", 0)

    assert data.get_value() == 5


def test_byte_write():
    """
    Check that writing a byte works as intended.
    """

    data = chao_examiner.ByteChunk("test", b"\x05", 0)
    assert data.get_value() == 5

    data.set_value(34)
    assert data.get_value() == 34

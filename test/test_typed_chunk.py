"""
Tests on loading chunks of binary data into usable data.
"""
import chao_examiner
import pytest


def test_byte():
    """
    Check that a byte works as intended.
    """

    data = chao_examiner.typed_chunk.ByteChunk.load("test", b"\x05", 0)
    assert data.get_value() == 5

    data.set_value(34)
    assert data.get_value() == 34


def test_signed_byte():
    """
    Check that a signed byte works as intended.
    """

    data = chao_examiner.typed_chunk.SignedByteChunk.load("test", b"\x05", 0)
    assert data.get_value() == 5

    data.set_value(34)
    assert data.get_value() == 34


def test_short():
    """
    Check that a short integer works as intended.
    """

    data = chao_examiner.typed_chunk.ShortChunk.load("test", b"\x05\x00", 0)
    assert data.get_value() == 5

    data.set_value(3425)
    assert data.get_value() == 3425


def test_int():
    """
    Check that a full integer works as intended.
    """

    data = chao_examiner.typed_chunk.IntChunk.load("test", b"\x05\x00\x00\x00", 0)
    assert data.get_value() == 5

    data.set_value(3425)
    assert data.get_value() == 3425


def test_float():
    """
    Check that a float works as intended.
    """

    data = chao_examiner.typed_chunk.FloatChunk.load("test", b"\x00\x80}C", 0)
    assert (data.get_value() - 253.5) < 0.0001

    data.set_value(3425.2)
    assert (data.get_value() - 3425.2) < 0.0001


def test_boolean():
    """
    Check that a boolean works as intended.
    """

    data = chao_examiner.typed_chunk.BooleanChunk.load("test", b"\x00", 0)
    assert not data.get_value()

    data.set_value(True)
    assert data.get_value()


def test_name():
    """
    Check that a chao name works as intended.
    """

    data = chao_examiner.typed_chunk.ChaoNameChunk.load(
        "test", b"\x01\x01\x01\x01\x01\x01\x01", 0
    )
    assert data.get_value() == "!!!!!!!"

    data.set_value("Test")
    assert data.get_value() == "Test"


def test_time():
    """
    Check that a time works as intended.
    """

    data = chao_examiner.typed_chunk.TimeChunk.load("test", b"\x01\x01\x01", 0)
    assert data.get_value() == "01:01:01"

    data.set_value("25:15:00")
    assert data.get_value() == "25:15:00"


def test_bytes_lookup():
    """
    Check that a single-byte lookup works as intended.
    """

    data = chao_examiner.typed_chunk.ByteLookup.load(
        "test", b"\x01", 0, {0: "A", 1: "B", 3: "C"}
    )
    assert data.get_value() == "B"

    data.set_value("C")
    assert data.get_value() == "C"


def test_int_flag_lookup():
    """
    Check that a integer flag lookup works as intended.
    """

    data = chao_examiner.typed_chunk.IntFlags.load(
        "test", b"\x03\x00\x00\x00", 0, {1: "A", 2: "B", 4: "C"}
    )

    table = data.get_value()

    assert table["A"] == True
    assert table["B"] == True
    assert table["C"] == False

    data.set_value({"A": True, "B": False, "C": True})
    assert data.get_value()["A"] == True
    assert data.get_value()["B"] == False
    assert data.get_value()["C"] == True


def test_short_flag_lookup():
    """
    Check that a integer flag lookup works as intended.
    """

    data = chao_examiner.typed_chunk.ShortFlags.load(
        "test", b"\x03\x00\x00\x00", 0, {1: "A", 2: "B", 4: "C"}
    )

    table = data.get_value()

    assert table["A"] == True
    assert table["B"] == True
    assert table["C"] == False

    data.set_value({"A": True, "B": False, "C": True})
    assert data.get_value()["A"] == True
    assert data.get_value()["B"] == False
    assert data.get_value()["C"] == True

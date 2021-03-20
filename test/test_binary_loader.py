import tempfile

import chao_examiner
import pytest

from .load_data import data_path, get_sha256


def test_load():
    """
    Check that data loading doesn't cause an error.
    """
    data = chao_examiner.BinaryLoader.read(data_path("SONIC2B__ALF"))
    assert len(data.binary) > 0


def test_load_save():
    """
    Check that a saved data file matches the original.
    """
    original_path = data_path("SONIC2B__ALF")

    data = chao_examiner.BinaryLoader.read(original_path)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = temp_dir + "/load_save"
        data.write(temp_path)

        assert get_sha256(original_path) == get_sha256(temp_path)


def test_extract_chunk():
    """
    Check extraction of a chunk from the binary data.
    """
    data = chao_examiner.BinaryLoader.read(data_path("SONIC2B__ALF"))
    chunk = data.chunk("Test", 0, 25)

    assert len(chunk.data) == 25

    chunk = data.chunk("Test", 100, 256)

    assert len(chunk.data) == 156


def test_chunk_clear():
    """
    Check extraction of a chunk from the binary data.
    """
    data = chao_examiner.BinaryLoader.read(data_path("SONIC2B__ALF"))
    chunk = data.chunk("Test", 0, 25)
    chunk.clear()
    assert int.from_bytes(chunk.data, byteorder="big") == 0


def test_chunk_update():
    """
    Check Updating a chunk of binary data works as intended.
    """
    data = chao_examiner.BinaryLoader.read(data_path("SONIC2B__ALF"))
    chunk = data.chunk("Test", 0, 25)

    new_data = b"\x01" * 25
    assert chunk.data != new_data
    chunk.update(new_data)

    assert chunk.data == new_data


def test_chunk_update_length_error():
    """
    Check that updating a chunk with the wrong length binary fails.
    """
    data = chao_examiner.BinaryLoader.read(data_path("SONIC2B__ALF"))
    chunk = data.chunk("Test", 0, 25)

    new_data = b"\x01" * 1

    with pytest.raises(ValueError):
        chunk.update(new_data)


def test_chunk_update_type_error():
    """
    Check that updating a chunk with a non-binary object fails.
    """
    data = chao_examiner.BinaryLoader.read(data_path("SONIC2B__ALF"))
    chunk = data.chunk("Test", 0, 25)

    new_data = "This string isn't a binary!"

    with pytest.raises(TypeError):
        chunk.update(new_data)


def test_chunk_inject():
    """
    Check that re-injecting a chunk of binary data into a BinaryLoader works.
    """
    data = chao_examiner.BinaryLoader.read(data_path("SONIC2B__ALF"))
    chunk = data.chunk("Test", 0, 25)

    new_data = b"\x01" * 25
    chunk.update(new_data)

    assert data.binary[0:25] != new_data
    chunk.inject(data)
    assert data.binary[0:25] == new_data


def test_chunk_inject_binary():
    """
    Check that re-injecting a chunk of binary data into a bytes object works.
    """
    data = chao_examiner.BinaryLoader.read(data_path("SONIC2B__ALF"))
    chunk = data.chunk("Test", 0, 25)

    new_data = b"\x01" * 25
    chunk.update(new_data)

    binary = data.binary

    assert binary[0:25] != new_data
    binary = chunk.inject(binary)
    assert binary[0:25] == new_data


def test_load_save_modified():
    """
    Check that a saved data file doesn't match the original after modification.
    """
    original_path = data_path("SONIC2B__ALF")
    data = chao_examiner.BinaryLoader.read(original_path)

    chunk = data.chunk("Test", 0, 25)
    new_data = b"\x01" * 25
    chunk.update(new_data)
    chunk.inject(data)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = temp_dir + "/load_save"
        data.write(temp_path)
        assert get_sha256(original_path) != get_sha256(temp_path)

        with open(temp_path, "rb") as file:
            raw = file.read()
        assert raw[0:25] == new_data

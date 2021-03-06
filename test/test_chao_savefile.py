import hashlib
import tempfile

import chao_examiner
import pytest

from .load_data import data_path, get_sha256


def load_savefile(data_name: str) -> chao_examiner.ChaoSaveFile:
    """
    Helper to load a SaveFile.
    """
    return chao_examiner.ChaoSaveFile(data_path(data_name))


def test_load():
    """
    Check that data loading doesn't cause an error.
    """
    data = chao_examiner.ChaoSaveFile(data_path("SONIC2B__ALF"))

    assert len(data.chao) == 24


def test_access_chao():
    """
    Check loading a Chao from the SaveFile.
    """
    data = load_savefile("SONIC2B__ALF")

    for chao_no in range(24):
        assert isinstance(data.get_chao(chao_no), chao_examiner.Chao)


def test_access_issues():
    """
    Check that accessing a chao outside of the allowed indexes throws an error.
    """
    data = load_savefile("SONIC2B__ALF")

    with pytest.raises(KeyError):
        data.get_chao(-1)

    with pytest.raises(KeyError):
        data.get_chao(25)


def test_set_chao():
    """
    Check that the chao setting functionality works as intended by swapping two Chao.
    """
    data = load_savefile("SONIC2B__ALF")

    slot_0_start = data.get_chao(0)
    slot_1_start = data.get_chao(1)

    assert slot_0_start.binary != slot_1_start.binary

    data.set_chao(slot_1_start, 0)
    data.set_chao(slot_0_start, 1)

    slot_0_end = data.get_chao(0)
    slot_1_end = data.get_chao(1)

    assert slot_0_end.binary != slot_1_end.binary
    assert slot_0_start.binary == slot_1_end.binary
    assert slot_1_start.binary == slot_0_end.binary


def test_clear_chao():
    """
    Check that clearing the data for a Chao works.
    """
    data = load_savefile("SONIC2B__ALF")

    slot_0_start = data.get_chao(0)
    data.clear_chao(0)
    slot_0_end = data.get_chao(0)

    assert slot_0_start.binary != slot_0_end.binary
    assert slot_0_end.binary == b"\x00" * data.data_length


def test_file_passthrough():
    """
    Check that pulling a chao out and putting it back is transparent.
    """

    original_path = data_path("SONIC2B__ALF")

    data = chao_examiner.ChaoSaveFile(original_path)
    chao = data.get_chao(0)
    data.set_chao(chao, 0)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = temp_dir + "/load_save"
        data.write(temp_path)

        other = chao_examiner.ChaoSaveFile(temp_path)
        for x in range(24):
            assert data.chao[x] == other.chao[x]

        assert get_sha256(original_path) == get_sha256(temp_path)


def test_file_modified():
    """
    Check that changes to the save file are properly stored.
    """

    original_path = data_path("SONIC2B__ALF")

    data = chao_examiner.ChaoSaveFile(original_path)
    chao = data.get_chao(0)
    chao["Name"] = "Test"
    assert chao["Name"] == "Test"
    data.set_chao(chao, 0)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = temp_dir + "/load_save"
        data.write(temp_path)

        other = chao_examiner.ChaoSaveFile(temp_path)
        assert other.get_chao(0)["Name"] == "Test"
        assert get_sha256(original_path) != get_sha256(temp_path)


def test_file_resaved():
    """
    Check that changes to the save file are properly stored and that modified files are
    identical to the input (to pick up any byte-encoding errors).
    """

    original_path = data_path("SONIC2B__ALF")

    # Load data & variables.
    start_sha = get_sha256(original_path)
    data = chao_examiner.ChaoSaveFile(original_path)
    chao = data.get_chao(0)
    start_name = chao["Name"]

    # Change the chao's name.
    chao["Name"] = "Test"
    assert chao["Name"] == "Test"
    data.set_chao(chao, 0)

    # Push the data through a save-file
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path_a = temp_dir + "/load_save"
        data.write(temp_path_a)
        intermediate = chao_examiner.ChaoSaveFile(temp_path_a)
        intermediate_sha = get_sha256(temp_path_a)

    # Change the chao's name back.
    chao = intermediate.get_chao(0)
    chao["Name"] = start_name
    assert chao["Name"] == start_name
    intermediate.set_chao(chao, 0)

    # And push to a final save file
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path_a = temp_dir + "/load_save"
        intermediate.write(temp_path_a)
        final_sha = get_sha256(temp_path_a)

    assert start_sha == final_sha
    assert start_sha != intermediate_sha

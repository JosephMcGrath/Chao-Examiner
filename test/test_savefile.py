import hashlib
import tempfile

import chao_examiner
import pytest

from .load_data import data_path


def load_savefile(data_name: str) -> chao_examiner.SaveFile:
    """
    Helper to load a SaveFile.
    """
    return chao_examiner.SaveFile(data_path(data_name))


def test_load():
    """
    Check that data loading doesn't cause an error.
    """
    data = chao_examiner.SaveFile(data_path("SONIC2B__ALF"))

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

from .load_data import data_path
import hashlib
import tempfile

import chao_examiner


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


def get_sha256(path: str) -> str:
    """Calculates a sha256 hash of the file."""
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()

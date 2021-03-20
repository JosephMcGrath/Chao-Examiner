"""
Handling test data.
"""

import os
import hashlib


def data_path(data_name: str) -> str:
    """
    Load test data.
    """
    data_path = os.path.join(os.path.split(__file__)[0], "data", data_name)
    assert os.path.exists(data_path)
    return data_path


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

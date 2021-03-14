"""
Handling test data.
"""

import os


def data_path(data_name: str) -> str:
    """
    Load test data.
    """
    data_path = os.path.join(os.path.split(__file__)[0], "data", data_name)
    assert os.path.exists(data_path)
    return data_path

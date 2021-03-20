"""
Module to load, examine and manipulate Chao data for Sonic Adventure 2 save data.
"""

from .binary_loader import BinaryLoader
from .chao import Chao
from .logs import LOG_NAME, setup_logging
from .chao_savefile import ChaoSaveFile

setup_logging(log_dir="")

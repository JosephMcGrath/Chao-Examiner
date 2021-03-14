"""
Module to load, examine and manipulate Chao data for Sonic Adventure 2 save data.
"""

from .binary_loader import BinaryLoader
from .logs import LOG_NAME, setup_logging

setup_logging(log_dir="")

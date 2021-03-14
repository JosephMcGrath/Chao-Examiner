"""
Defines logging setup.
"""
import logging
import logging.config
import os
from typing import Any, Dict, Optional

LOG_NAME = __name__


def setup_logging(log_dir: Optional[str] = None) -> None:
    """
    Set up a log pointing at the specified path.
    """
    config: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {"console": {"format": "%(asctime)s:\t%(message)s"}},
        "handlers": {
            "console": {
                "level": "WARNING",
                "class": "logging.StreamHandler",
                "formatter": "console",
                "stream": "ext://sys.stdout",
            }
        },
        "loggers": {
            LOG_NAME: {"handlers": ["console"], "level": "DEBUG", "propagate": False}
        },
    }
    if log_dir is not None:
        config["loggers"][LOG_NAME]["handlers"].append("file")
        config["formatters"]["file"] = {
            "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        }
        config["handlers"]["file"] = {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "file",
            "filename": os.path.join(log_dir, LOG_NAME + ".log"),
            "maxBytes": 1000000,
            "backupCount": 3,
        }
    logging.config.dictConfig(config)

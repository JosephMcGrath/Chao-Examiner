"""
Command-line tool to convert a Chao file to JSON extracts.
"""

import argparse
import logging
import os

from .chao_savefile import ChaoSaveFile
from .logs import LOG_NAME


def chao_to_json() -> None:
    """
    Run the tool via command-line tools.
    """

    parser = argparse.ArgumentParser(description="Markdown notebook manager.")
    parser.add_argument("-source_dir", type=str, help="Save file folder.")
    parser.add_argument(
        "-output_dir", type=str, help="Destination folder.", default=os.getcwd()
    )
    args = parser.parse_args()

    if args.source_dir is None:
        print("Need to specify a source path.")
        return

    output_dir = args.output_dir
    if os.path.splitext(output_dir)[-1] == "":
        logging.getLogger(LOG_NAME).warning(
            "Output is a directory - writing to chao.json in the folder."
        )
        output_dir = os.path.join(output_dir, "chao.json")

    ChaoSaveFile.find(args.source_dir).to_json(output_dir)


if __name__ == "__main__":
    chao_to_json()

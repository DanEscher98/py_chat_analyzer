import os
import argparse
from argparse import Namespace


def file_exists(file_path):
    if not os.path.exists(file_path):
        raise argparse.ArgumentTypeError(f"File '{file_path}' does not exist.")
    return file_path


def get_args() -> Namespace:
    parser = argparse.ArgumentParser(
        prog="wa_txt2md",
        usage="%(prog)s [options] FILE",
        description="Process Whatsapp's .txt conversations",
    )
    parser.add_argument("FILE", type=file_exists,
                        help="Whatsapp's txt file to process")
    return parser.parse_args()

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
    parser.add_argument("-n", "--name", default="a Person",
                        help="The name")
    parser.add_argument("-j", "--json", action="store_true",
                        help="Enable json generation")
    return parser.parse_args()

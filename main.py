#!/usr/bin/env python3

import argparse
import concurrent.futures
import logging

from read_file import safe_load
from count_islands import Array, CountIslands

PATH_TO_FILE = "islands.txt"

log = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="This program calculates number of islands from given file")
    parser.add_argument("file", nargs="?", default=PATH_TO_FILE)
    args = parser.parse_args()

    return args


def main():

    args = parse_args()
    array = safe_load(args.file)

    if array:
        a = Array(array)
        islands = CountIslands(a)
        with concurrent.futures.ProcessPoolExecutor() as executor:
            ret = executor.submit(islands.count_islands)

        print(f"Number of islands: {ret.result()}")


if __name__ == "__main__":
    main()

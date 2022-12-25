import argparse
import concurrent.futures

from read_file import safe_load
from count_islands import Array, CountIslands

PATH_TO_FILE = "islands.txt"


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
    else:
        print("No data in array")


if __name__ == "__main__":
    main()

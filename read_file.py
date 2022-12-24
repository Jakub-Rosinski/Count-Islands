
from typing import List

PATH_TO_FILE = "islands.txt"

# check data for characters other than "1", "0"
# check if empty file
# check if .txt
# check if readable


def check_data(array: List[List[str]]) -> bool:
    """Checks if array is rectangular"""
    return all([len(row) == len(array[0]) for row in array])


def read_file_to_array() -> List[List[str]]:
    """
    Reads data from given file and transforms data into array

    :returns: Two dimensional array with strings
              Example: ['0', '0', '0', '0', '0', '0', '0', '0', '0']
                       ['0', '1', '0', '0', '0', '0', '0', '0', '0']
                       ['1', '1', '1', '0', '0', '0', '1', '0', '0']
                       ['1', '1', '0', '0', '0', '1', '1', '1', '0']
                       ['0', '0', '0', '0', '0', '1', '1', '0', '0']
                       ['0', '0', '1', '0', '0', '0', '0', '0', '0']
                       ['1', '1', '0', '0', '0', '0', '0', '0', '0']
                       ['0', '0', '0', '0', '0', '1', '1', '0', '0']
    """

    array = []
    for line in open(PATH_TO_FILE):
        line = list(line.rstrip())
        array.append(line)

    if check_data(array):
        return array
    return []

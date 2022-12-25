import os
from typing import List


def if_file_exists(path: str) -> bool:
    """Checks if file exists"""
    return os.access(path, os.F_OK)


def if_file_readable(path: str) -> bool:
    """Checks if file us readable"""
    return os.access(path, os.R_OK)


def if_file_not_empty(path: str) -> bool:
    """Checks if file is not empty"""
    return os.stat(path).st_size != 0


def if_array_rectangular(array: List[List[str]]) -> bool:
    """Checks if array is rectangular"""
    return all(len(row) == len(array[0]) for row in array)


def if_data_consistent(line: List[str]) -> bool:
    """Checks if data in array are consistent meaning each element is either "0" or "1" """
    return all(el in ["0", "1"] for el in line)


def read_file_to_array(path: str) -> List[List[str]]:
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
    for line in open(path):
        line = list(line.rstrip())
        if if_data_consistent(line):
            array.append(line)
        else:
            return []

    if if_array_rectangular(array):
        return array
    return []


def safe_load(path: str) -> List[List[str]]:
    conditions = [if_file_exists(path),
                  if_file_readable(path),
                  if_file_not_empty(path)]

    if all(conditions):
        data = read_file_to_array(path)
        return data
    return []

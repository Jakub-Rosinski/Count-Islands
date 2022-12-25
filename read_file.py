import logging
import os
from typing import List

log = logging.getLogger(__name__)


class FileNotExist(Exception):
    pass


class FileNotReadable(Exception):
    pass


class FileEmpty(Exception):
    pass


def if_file_exists(path: str) -> bool:
    """Checks if file exists"""
    if os.access(path, os.F_OK):
        return True
    raise FileNotExist(f"File '{path}' does not exist")


def if_file_readable(path: str) -> bool:
    """Checks if file us readable"""
    if os.access(path, os.R_OK):
        return True
    raise FileNotReadable(f"File '{path}' is not readable")


def if_file_not_empty(path: str) -> bool:
    """Checks if file is not empty"""
    if os.stat(path).st_size != 0:
        return True
    raise FileEmpty(f"File '{path}' is empty")


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
            log.error("Inconsistent data")
            return []

    if if_array_rectangular(array):
        return array

    log.error("Incorrect structure of data - array must be rectangular")
    return []


def safe_load(path: str) -> List[List[str]]:
    try:
        if_file_exists(path)
        if_file_readable(path)
        if_file_not_empty(path)

        data = read_file_to_array(path)
        return data
    except (FileNotExist, FileNotReadable, FileEmpty) as err:
        log.error(err)
    except Exception as e:
        log.error(f"Cannot read data from file {path} - error: {e}")
    return []

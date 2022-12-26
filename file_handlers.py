import os


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

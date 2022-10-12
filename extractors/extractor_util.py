import os
import fnmatch


def ensure_exist(path: str):
    exists: bool = os.path.exists(path)
    if not exists:
        os.makedirs(path)


def count_file_in_dir(path):
    count = len(fnmatch.filter(os.listdir(path), '*.*'))
    return count

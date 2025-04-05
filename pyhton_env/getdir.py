#!/usr/bin/env python

from pathlib import Path

def get_file_path(filename):
    return str(Path(filename).resolve())

# Example usage
file_path = get_file_path("pyhthon_env/getdir.py")
print("the path is", file_path)
#!/usr/bin/python3
""" The module contains a read_file(filename="") reads text file
    Prototype: def read_file(filename=""):
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
    You are not allowed to import any module
    """


def read_file(filename=""):
    """Reads text file (utf-8) format and print out to stdout

    Args:
        filename (str, optional): The path to the file to be read.
            Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

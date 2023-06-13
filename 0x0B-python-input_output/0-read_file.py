#!/usr/bin/python3
"""
Module: file_reader

This module provides a function for reading a text file and printing its contents to stdout.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF-8 encoded) and prints its contents to stdout.

    Args:
        filename (str, optional): The name of the file to be read. Defaults to "".

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents)
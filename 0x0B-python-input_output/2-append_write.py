#!/usr/bin/python3
"""
Module: file_appender

This module provides a function for appending a string to
the end of a text file (UTF-8 encoded)
and returning the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8 encoded)
    and returns the number of
    characters added.

    Args:
        filename (str, optional): The name of the file to append to.
        Defaults to "".
        text (str, optional): The string to append to the file.
        Defaults to "".

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        num_chars_added = file.write(text)
    return num_chars_added

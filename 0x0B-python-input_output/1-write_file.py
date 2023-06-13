#!/usr/bin/python3
"""
Module: file_writer

This module provides a function for writing a string to a text file
(UTF-8 encoded) and returning the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8 encoded) and returns
    the number of characters written.

    Args:
        filename (str, optional): The name of the file to write to.
        Defaults to "".
        text (str, optional): The string to write to the file.
        Defaults to "".

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
    return num_chars_written

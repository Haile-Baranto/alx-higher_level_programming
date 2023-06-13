#!/usr/bin/python3
"""
Module: json_file_writer

This module provides a function for writing an object
to a text file using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to write to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)

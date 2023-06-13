#!/usr/bin/python3
"""
Module: json_file_reader

This module provides a function for creating an
object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, "r") as file:
        obj = json.load(file)
    return obj

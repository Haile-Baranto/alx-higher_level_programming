#!/usr/bin/python3
"""
Module: json_parser

This module provides a function for parsing a JSON string and
returning the corresponding Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns the object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to parse.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)

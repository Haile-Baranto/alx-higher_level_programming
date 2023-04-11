#!/usr/bin/python3
import json
""" The function converts from json to string
    Prototype: def from_json_string(my_str):
    You don’t need to manage exceptions if the JSON
        string doesn’t represent an object.
    """


def from_json_string(my_str):
    """
    Returns the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to parse.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)

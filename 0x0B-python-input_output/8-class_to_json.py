#!/usr/bin/python3
"""
json_serializer

This module provides a function for JSON serialization of
objects with simple data structures.

The function `class_to_json` takes an object as input and
returns a dictionary representation of the
object's attributes suitable for JSON serialization.
Only attributes with simple data structures such
as lists, dictionaries, strings, integers, and booleans are
included in the dictionary.

"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj (object): An instance of a Class.

    Returns:
        dict: The dictionary description representing the serialized object.
    """
    json_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict

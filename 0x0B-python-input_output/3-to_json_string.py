#!/usr/bin/python3
import json
""" The module contains to_json_string function that converts
        python data to json
    Prototype: def to_json_string(my_obj):
    You don’t need to manage exceptions if the object can’t be serialized.
    """


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Args:
        my_obj (object): The object to convert to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)

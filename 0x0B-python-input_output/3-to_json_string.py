#!/usr/bin/python3
import json
""" The module contains to_json_string function that converts
        python data to json
    Prototype: def to_json_string(my_obj):
    You don’t need to manage exceptions if the object can’t be serialized.
    """


def to_json_string(my_obj):
    """to_json_string  returns the JSON representation of an object (string)

    Args:
        my_obj (obj): python object to be converted to json

    Returns:
        json: json representation of my_obj
    """
    return (json.dumps(my_obj))

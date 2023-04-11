#!/usr/bin/python3
import json
""" The module contains to_json_string function that converts
        python data to json
    Prototype: def to_json_string(my_obj):
    You don’t need to manage exceptions if the object can’t be serialized.
    """
import json


def to_json_string(my_obj):
    """to_json_string  returns the JSON representation of an object (string)

    Args:
        my_obj (obj): any object for example list, dict
    """
    return(json.dumps(my_obj))


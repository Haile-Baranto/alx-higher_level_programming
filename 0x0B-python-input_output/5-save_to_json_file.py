#!/usr/bin/python3
import json
"""Prototype: def save_to_json_file(my_obj, filename):
    You must use the with statement
    You don’t need to manage exceptions if the object can’t be serialized.
    You don’t need to manage file permission exceptions.
    """


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a file in JSON format.

    Args:
        my_obj (object): The object to write to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

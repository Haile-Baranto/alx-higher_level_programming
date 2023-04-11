#!/usr/bin/python3
"""Prototype: def class_to_json(obj):
    obj is an instance of a Class
    All attributes of the obj Class are serializable: list,
        dictionary, string, integer and boolean
    You are not allowed to import any module

    """


def class_to_json(obj):
    """Returns a dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: A dictionary description with simple data structure for JSON
        serialization.
    """
    if not hasattr(obj, "__dict__"):
        return obj

    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, tuple)):
            result[key] = [class_to_json(item) for item in value]
        elif isinstance(value, dict):
            result[key] = {
                k: class_to_json(v) for k, v in value.items()
            }
        elif isinstance(value, str):
            result[key] = value
        elif isinstance(value, bool):
            result[key] = value
        elif isinstance(value, int):
            result[key] = value
        else:
            result[key] = class_to_json(value)

    return result

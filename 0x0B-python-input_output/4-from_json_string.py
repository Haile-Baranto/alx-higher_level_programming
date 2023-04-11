#!/usr/bin/python3

import json

""" The module contains from_json_string that converts
    json file to python data sructure
    Prototype: def from_json_string(my_str):
    You don’t need to manage exceptions if the JSON string
        doesn’t represent an object.
    """


def from_json_string(my_str):
    return json.loads(my_str)

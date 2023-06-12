#!/usr/bin/python3
"""The function that returns available methods and attributes
    of an object.
    Prototype: def lookup(obj):
    Returns a list object
    You are not allowed to import any module
    """


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)

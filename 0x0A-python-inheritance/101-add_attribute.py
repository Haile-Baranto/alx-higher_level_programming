#!/usr/bin/python3
""" The module contains adds a new attribute to an object if it’s possible:
    You are not allowed to use try/except
    You are not allowed to import any module
    """


def add_attribute(obj, name, value):
    """ Adds a new attribute to an object if it’s possible:

    Raises:
        TypeError: The error raises if adding attribute is possible
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")

#!/usr/bin/python3
""" The module contains a function to check if an object is
    an exact instance of a given class
    Prototype: def is_kind_of_class(obj, a_class):
    You are not allowed to import any module
    """


def is_same_class(obj, a_class):
    """Checks if an oject is exact instance of a given class

    Args:
        obj (obj): an instance of a class
        a_class (cls): class to be checked if obj is
        its instance

    Returns:
        bool: if is instance True else False
    """
    if type(obj) is a_class:
        return True
    return False

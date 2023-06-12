#!/usr/bin/python3
""" The module contains a function to check if an object is
    an instance of a given class
    Prototype: def is_kind_of_class(obj, a_class):
    You are not allowed to import any module
    """


def is_kind_of_class(obj, a_class):
    """The function returns True if the object is an
    instance of, or if the object is an instance of a class that
    inherited from, the specified class ; otherwise False.

    Args:
        obj (obj): an instance of a class
        a_class (cls): class or super class to be checked if obj is
        its instance
    """
    return isinstance(obj, a_class)

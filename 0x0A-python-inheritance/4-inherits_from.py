#!/usr/bin/python3
""" Prototype: def inherits_from(obj, a_class):
    You are not allowed to import any module
    """


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class;
    otherwise False.
    """
    if (type(obj) != a_class and issubclass(type(obj), a_class)):
        return True
    return False

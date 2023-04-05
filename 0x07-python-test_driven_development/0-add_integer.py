#!/usr/bin/python3
# File: 0-add_integer.py
""" The module contains add(a, b = 89) that adds two ingers
    Prototype: def add_integer(a, b=98):
    You are not allowed to import any module
    """


def add_integer(a, b=98):
    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise ValueError("a must be an integer")
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        raise ValueError("b must be an integer")
    return int(a) + int(b)

#!/usr/bin/python3
# File: 0-add_integer.py
""" The module contains add(a, b = 89) that adds two integers
    Prototype: def add_integer(a, b=98):
    You are not allowed to import any module
    """


def add_integer(a, b=98):
    """
    Adds two integers.

    :param a: An integer or float.
    :param b: An integer or float. Default value is 98.
    :return: The addition of `a` and `b` as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

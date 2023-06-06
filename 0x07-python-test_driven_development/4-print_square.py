#!/usr/bin/python3
# 4-print_square.py
""" File name : 4-print_square.py
    Print_square(size): function that print # size * size
    Prototype: def print_square(size)
    You are not allowed to import any module
"""


def print_square(size):
    """function that prints a square with the character #
    size: numbers the character # to print
    Raises:
        TypeError: size must be an integer
        TypeError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    hastag = "#"
    hastag = size * hastag
    for i in range(size):
        print("{}".format(hastag))

#!/usr/bin/python3
""" File name : 3-say_my_name.py
    Say my name: function that prints My name is <first name> <last name>
    Prototype: def say_my_name(first_name, last_name="")
    You are not allowed to import any module
"""


def say_my_name(first_name, last_name=""):
    """prints out My name is <first name> <last name>

    Args:
        first_name (str): First name of the person
        last_name (str, optional): Last name of the person. Defaults to "".

    Raises:
        TypeError: first_name must be string
        TypeError: last_name must be string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

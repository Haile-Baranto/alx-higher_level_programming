#!/usr/bin/python3
"""The module conatains a class BaseGeometry (based on 6-base_geometry.py).
    You are not allowed to import any module
    """


class BaseGeometry:
    """
    """
    def area(self):
        """that raises an Exception with the message area() is not implemented

        Raises:
            Exception: exception to be raised when area is not defined
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value as an integer greater than 0.

        Args:
            name (str): string
            value (_int): value to be validated

        Raises:
            TypeError: make sure value to be integer
            ValueError: Make sure value to be > 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

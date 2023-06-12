#!/usr/bin/python3
"""The module conatain BaseGeometry class (based on 5-base_geometry.py).
    You are not allowed to import any module
    """


class BaseGeometry:
    """that raises an Exception with the message area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")

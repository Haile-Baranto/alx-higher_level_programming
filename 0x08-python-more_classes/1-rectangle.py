#!/usr/bin/python3
""" File name : 1-rectangle.py
    Real definiton of rectangle
    It is not allowed to import any module
"""


class Rectangle(object):
    """Define new class Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize new class rectangle

        Args:
            width (int): width for the new rectangle
            height (int): height for the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """attribute width of instance of class rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set values to width property

        Args:
            value (int): value for property width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property for attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the values to height

        Args:
            value (int): value for height property
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

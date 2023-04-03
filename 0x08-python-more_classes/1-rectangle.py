#!/usr/bin/python3
# creates an empty class
""" Define class Rectangle
    Using module is not allowed"""


class Rectangle(object):
    """ defines new class Rectangle"""
    def __init__(self, width=0, height=0):
        """Instanciates the object with width and height

        Args:
            width (int, optional): height of new rectangle. Defaults to 0.
            height (int, optional): width of the new rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getts width property

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width property

        Args:
            value (int): _the vaue to be set to width

        Raises:
            ValueError: if vaue is not int
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns private property height

        Returns:
            int: height to be returned
        """
        return self.__width

    @height.setter
    def height(self, value):
        """setts instance attribute height

        Args:
            value (int): the value to be set

        Raises:
            ValueError: if height is not integer
            ValueError: if height is negative
        """
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

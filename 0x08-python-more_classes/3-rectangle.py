#!/usr/bin/python3
""" File name : 3-rectangle.py
    Defines Rectangle
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
        self.height = height
        self.width = width

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

    def area(self):
        """Defines area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Defines perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ string representation of square """
        if self.width == 0 or self.height == 0:
            return ""
        y = "#" * self.width
        rectangle = y
        for i in range(self.height - 1):
            rectangle += "\n" + y
        return rectangle

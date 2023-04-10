#!/usr/bin/python3
""" The module contains class Square that inherits from
        Rectangle (9-rectangle.py
    importing any module is not allowed
    """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherits from super class Rectangle

    Args:
        Rectangle (cls): class of type Rectangle
    """

    def __init__(self, size):
        """intantiate the class Square

        Args:
            size (int): height or width of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of rectangle

        Returns:
            int: rectangle area
        """
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

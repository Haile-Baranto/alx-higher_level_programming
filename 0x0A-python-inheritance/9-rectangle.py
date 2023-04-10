#!/usr/bin/python3
""" The module contains class Rectangle that inherits from
        BaseGeometry (7-base_geometry.py).
    importing any module is not allowed
    """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inherits from super class BaseGeomery

    Args:
        BaseGeometry (cls): class of type BaseGeometry
    """
    def __init__(self, width, height):
        """instantiates both height and width of rectangles
        after it validates both are integer > 0

        Args:
            width (_int): width if rectangle
            height (_int): _height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of rectangle

        Returns:
            int: rectangle area
        """
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

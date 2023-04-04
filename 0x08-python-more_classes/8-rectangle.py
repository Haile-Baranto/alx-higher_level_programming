#!/usr/bin/python3
""" File name : 8-rectangle.py
    Based on 7-rectangle.py
    Static method def bigger_or_equal(rect_1, rect_2)
    compare two rectanles of instance of Rectangle
    It is not allowed to import any module
"""


class Rectangle(object):
    """Rectangle: Define new class"""
    # public class property
    number_of_instances = 0
    # print_symbol: used as symbol for srring represntation
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize new class rectangle

        Args:
            width (int): width for the new rectangle
            height (int): height for the new rectangle
        """
        self.height = height
        self.width = width
        # Increamts each time we create an instance
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """attribute width of instance of class rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set values to width

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
        """Defines area"""
        return self.__width * self.__height

    def perimeter(self):
        """Defines perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for i in range(self.__height):
            for i in range(self.__width):
                rect += str(self.print_symbol)
            rect += '\n'
        rect = rect[:-1]
        return rect

    def __repr__(self):
        """String representation of the rectangle"""
        return "Rectangle({}, {})".format(str(self.width), str(self.height))

    def __del__(self):
        """prints "By rectangle ..." whenever we delete
        instance of Rectangle class
        """
        print("Bye rectangle...")
        # Decrease each time we delete instance
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns rectangle with biggest area

        Args:
            rect_1 (Rectangle): First rectangle
            rect_2 (_type_): second rectangle

        Raises:
            TypeError: rect_1 is not instance of Rectangle
            TypeError: rect_1 is not instance of Rectangle

        Returns:
            int: rectangle with the largest area and if equal rect_1
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("ect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

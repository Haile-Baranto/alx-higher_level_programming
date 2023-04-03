#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        """Instanciates the object with width and height

        Args:
            width (int, optional): height of rectangle. Defaults to 0.
            height (int, optional): width of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

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
        if type(value) != int:
            raise ValueError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """setts width instance attribute

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width

        Args:
            value (int): _the vaue to be set to width

        Raises:
            ValueError: if vaue is not int
            ValueError: if value is < 0
        """
        if type(value) != int:
            raise ValueError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

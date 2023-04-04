#!/usr/bin/python3
class Rectangle(object):
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
        if isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
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
        if isinstance(value, int):
            raise ValueError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """public instance method calculates area of rectangle

        Returns:
            int: area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """computes premeiter of rectangle

        Returns:
            int: _area of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

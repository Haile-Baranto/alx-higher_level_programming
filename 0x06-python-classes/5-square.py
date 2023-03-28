#!/usr/bin/python3
""""Define a class Square"""


class Square:
    """Represent Square"""

    def __init__(self, size=0):
        """Initialize new square

        Args:
            size (int): The size of the new square
        """
        self.__size = size

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setts the size of the object

        Args:
            value (int): the value to be sett to size

        Raises:
            TypeError: error to be raized if value is not inger
            ValueError: error to be raised if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints the sqaure using # to stdout
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print("")
            print("")

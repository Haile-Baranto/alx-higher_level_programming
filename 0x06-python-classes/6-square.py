#!/usr/bin/python3
""""Define a class Square"""


class Square:
    """Represent Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize object of type Square

        Args:
            size (int, optional): size of the sqaure
            position (tuple, optional):position where to print
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Property for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets positions"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print vector with # and spaces"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

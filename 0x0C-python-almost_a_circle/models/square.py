#!/usr/bin/python3
""" Define a class Rectangle that inherits from rectangle
    File name - square.py
    """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square - class that inherits Rectangle class

    Args:
        Rectangle (class): base class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor:
        No new attribute will be created for this class
        you have to use all attribute of Rectangle class
        with width and height both assigned the value of
        size

        Args:
            size (int): width or height of square
            x (int, optional): x value. Defaults to 0.
            y (int, optional): y value. Defaults to 0.
            id (_type_, optional): id of an object. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of an object

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """Gets value for size

        Returns:
        int: size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of width and height with size

        Args:
            size (int): value to be set to width or height of square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """*args is the list of arguments - no-keyworded arguments
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
        **kwargs must be skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the instance
        """
        if args and len(args) != 0:
            len_of_args = len(args)
            if len_of_args >= 1:
                self.id = args[0]
            if len_of_args >= 2:
                self.size = args[1]
            if len_of_args >= 3:
                self.x = args[2]
            if len_of_args >= 4:
                self.y = args[3]
        elif len(kwargs) != 0 and kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        super().__init__(self.width, self.height,
                                         self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

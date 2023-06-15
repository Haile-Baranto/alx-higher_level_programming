#!/usr/bin/python3
"""This module defines the Rectangle class that represents a rectangle shape.

The Rectangle class is a subclass of the Base class and provides
methods for manipulating and displaying rectangles.

Classes:
    - Rectangle: Represents a rectangle and provides methods
    for manipulation and display.

Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    - x (int): The x-coordinate of the rectangle's position.
    - y (int): The y-coordinate of the rectangle's position.
    - id (int): The unique identifier of the rectangle.

Methods:
    - __init__(self, width, height, x=0, y=0, id=None):
    Initializes a Rectangle object.
    - area(self): Calculates the area of the rectangle.
    - display(self): Displays the rectangle using '#' characters.
    - __str__(self): Returns a string representation of the rectangle.
    - update(self, *args, **kwargs): Updates the attributes of the rectangle.
    - to_dictionary(self): Returns a dictionary representation of the
    rectangle.
    """
from models.base import Base


class Rectangle(Base):
    """Rectangle class define rectangle

    Args:
        Base (class): parent(super) class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ constructor that intialize the object.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): . Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id ([type], optional): id of the rectangle. Defaults to None.
        """
        # type check for width, height, x and y
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        # value check for width, height, x and y
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of rectangle

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """sets width of rectangle

        Args:
            width (int): width of rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Gets height of rectangle

        Returns:
            int: rectangle height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """sets height of rectangle

        Args:
            height (int): height of rectangle
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Gets value of x

        Returns:
            int: value of x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """sets value of x

        Args:
            x (int): value to be set

        Raises:
            TypeError: make sure x is int
            ValueError: make sure x is not negative
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Gets the value of y

        Returns:
            int: y value
        """
        return self.__y

    @y.setter
    def y(self, y):
        """sets value of y

        Args:
            y (int): value to be set

        Raises:
            TypeError: make sure y is int
            ValueError: make sure y is not negative
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    # public instance method area
    def area(self):
        """compute area of rectangle

        Returns:
            int: area of rectangle
        """
        return self.height * self.width

    def display(self):
        """ print in stdout the Rectangle instance with the character #
            by taking care of x and y
        """
        for i in range(self.__height):
            if i == 0:
                for vertical in range(self.y):
                    print()
            for j in range(self.__width):
                if j == 0:
                    for horizontal in range(self.x):
                        print(" ", end="")
                print("#", end="")
            print()

    def __str__(self):
        """String representation of rectangle object

        Returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
            Each key in kwargs represents an attribute to the instance
            kwargs must be skipped if *args exists and is not empty
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
                """
        if args and len(args) != 0:
            len_of_args = len(args)
            if len_of_args >= 1:
                self.id = args[0]
            if len_of_args >= 2:
                self.width = args[1]
            if len_of_args >= 3:
                self.height = args[2]
            if len_of_args >= 4:
                self.x = args[3]
            if len_of_args >= 5:
                self.y = args[4]
        elif len(kwargs) != 0 and kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        super().__init__(self.width, self.height,
                                         self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """

        Returns:
            _type_: _description_
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

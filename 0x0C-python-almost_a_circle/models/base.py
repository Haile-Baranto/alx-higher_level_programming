#!/usr/bin/python3
import json
import csv
import turtle
""" The module defines a base class Base
    Module name: base.py
    The the goal of the class is to manage id attribute of all
    comming classes.
    """


class Base:
    """Base: class define a class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Intialize Base class

        Args:
            id (int, optional): an int number. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (dict): a list of ditionary

        Returns:
            JSON: "[]" if list_dictionaries is empty else
            the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError(f"Invalid class name: {cls.__name__}")
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                json_string = f.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**dict_) for dict_ in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="") as file:
                reader = csv.reader(file)
                obj_list = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj_dict = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4]),
                        }
                    elif cls.__name__ == "Square":
                        obj_dict = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3]),
                        }
                    obj_inst = cls.create(**obj_dict)
                    obj_list.append(obj_inst)
                return obj_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y,
                    ]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(row)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares using
        Turtle graphics module.

        Args:
            list_rectangles (list): List of Rectangle objects.
            list_squares (list): List of Square objects.
        """
        screen = turtle.Screen()
        screen.setup(800, 600)  # Set the window size as per your preference
        pen = turtle.Turtle()

        # Draw Rectangles
        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)

        # Draw Squares
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        turtle.done()

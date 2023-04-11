#!/usr/bin/python3
"""
    You can assume json will always be a dictionary
    A dictionary key will be the public attribute name
    A dictionary value will be the value of the public attribute
    You are not allowed to import any module
    """


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student object.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student.

        Args:
            attrs (list): A list of attribute names to retrieve. If None, all
                attributes will be retrieved. Default is None.

        Returns:
            dict: A dictionary representing the student object.
        """
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): A dictionary representing the new attributes.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)

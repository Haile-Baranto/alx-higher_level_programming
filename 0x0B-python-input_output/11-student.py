#!/usr/bin/python3

"""
Student

This module provides a Student class that represents a student.

Example:
    # Create a new student
    student = Student("John", "Doe", 20)

    # Retrieve the dictionary representation of the student
    student_dict = student.to_json()

    # Replace attributes of the student from a dictionary
    json_data = {"first_name": "Jane", "last_name": "Smith", "age": 22}
    student.reload_from_json(json_data)

"""


class Student:
    """
    Student class that defines a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
            Defaults to None.

        Returns:
            dict: The dictionary representation of the student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with
        values from a dictionary.

        Args:
            json (dict): A dictionary containing attribute-value pairs.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)

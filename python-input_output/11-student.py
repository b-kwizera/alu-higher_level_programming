#!/usr/bin/python3
"""
Defines Student class with flexible to_json and reload_from_json methods.
"""


class Student:
    """
    Student class with public attributes and serialization methods.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.

        If attrs is a list of strings, returns only those attributes
        present in the list and in the instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: Dictionary of attribute names and values.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on the json.

        Args:
            json (dict): Dictionary containing keys matching attribute names
                         and their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)

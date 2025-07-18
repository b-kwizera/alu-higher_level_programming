#!/usr/bin/python3
"""
Defines a Student class with public attributes and a flexible to_json method.
"""


class Student:
    """
    Student class with public attributes: first_name, last_name, age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
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
            # Filter attributes based on attrs list
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        # Otherwise return all attributes
        return self.__dict__.copy()

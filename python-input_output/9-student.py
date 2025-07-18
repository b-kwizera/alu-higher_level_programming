#!/usr/bin/python3
"""
Defines a Student class with first_name, last_name, age and
a method to return JSON serializable dictionary representation.
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

    def to_json(self):
        """
        Returns the dictionary representation of the Student instance.

        Returns:
            dict: Dictionary with keys first_name, last_name, age
        """
        return self.__dict__.copy()

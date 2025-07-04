#!/usr/bin/python3
"""
This module defines a BaseGeometry class.
It provides base functionality for geometric shapes with area calculation
and integer validation methods.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    This class provides common functionality for geometric shapes including
    area calculation (not implemented) and integer validation for parameters.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        This method is not implemented in the base class and must be
        overridden by subclasses. Raises an Exception when called.

        Raises:
            Exception: Always raised with message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the parameter being validated
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

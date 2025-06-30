#!/usr/bin/python3
"""Defines BaseGeometry class with unimplemented area method."""


class BaseGeometry:
    """BaseGeometry class with area method that raises an Exception."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

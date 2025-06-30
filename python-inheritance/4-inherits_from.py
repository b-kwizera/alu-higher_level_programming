#!/usr/bin/python3
"""Defines a function to check if an object is an instance of a subclass of a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherits from a_class.

    Args:
        obj: The object to check.
        a_class: The class to check inheritance from.

    Returns:
        True if obj is instance of a subclass of a_class (not a_class itself), else False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

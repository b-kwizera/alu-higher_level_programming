#!/usr/bin/python3
"""Defines a function to check if an object is an instance of a class or its subclass."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is instance or subclass instance of a_class, else False.
    """
    return isinstance(obj, a_class)

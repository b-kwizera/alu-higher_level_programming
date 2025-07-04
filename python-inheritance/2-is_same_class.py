#!/usr/bin/python3
"""
This module provides a function to check if an object is exactly
an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    This function returns True if the object is exactly an instance of
    the specified class (not a subclass), otherwise False.

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class

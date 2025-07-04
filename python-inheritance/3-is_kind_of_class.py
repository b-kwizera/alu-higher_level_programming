#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of or inherits from the specified class.

    This function returns True if the object is an instance of the specified
    class or if the object is an instance of a class that inherited from
    the specified class, otherwise False.

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj is an instance of a_class or inherits from it,
              False otherwise
    """
    return isinstance(obj, a_class)

#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of
a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited from the
    specified class.

    This function returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class, but not if
    the object is an instance of the specified class itself.

    Args:
        obj: The object to check
        a_class: The class to check inheritance from

    Returns:
        bool: True if obj's class inherits from a_class (but is not
              a_class itself), False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

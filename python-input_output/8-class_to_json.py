#!/usr/bin/python3
"""
Function to return the dictionary description with simple data structure
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj (object): An instance of a class

    Returns:
        dict: Dictionary of the object's attributes suitable
    """
    return obj.__dict__.copy()

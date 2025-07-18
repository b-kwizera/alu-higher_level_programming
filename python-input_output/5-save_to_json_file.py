#!/usr/bin/python3
"""This module provides a function that writes an object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using its JSON representation."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

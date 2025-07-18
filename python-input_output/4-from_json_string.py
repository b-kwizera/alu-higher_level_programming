#!/usr/bin/python3
"""This module provides a function that returns an object by a JSON string."""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string."""
    return json.loads(my_str)

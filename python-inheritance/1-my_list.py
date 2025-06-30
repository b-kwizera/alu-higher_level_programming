#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""


class MyList(list):
    """MyList inherits from the built-in list class.

    Provides a method to print the list in sorted (ascending) order.
    """

    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the original list."""
        print(sorted(self))

#!/usr/bin/python3
"""Module that defines MyList class inheriting from list."""


class MyList(list):
    """Class that extends the built-in list with a sorted print method."""

    def print_sorted(self):
        """Prints the elements of the list in ascending sorted order."""
        print(sorted(self))

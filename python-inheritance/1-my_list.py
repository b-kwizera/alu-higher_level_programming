#!/usr/bin/python3
"""
This module defines a MyList class that inherits from list.
It provides additional functionality to print the list in sorted order.
"""


class MyList(list):
    """
    A class that inherits from list and provides additional functionality.
    
    This class extends the built-in list class by adding a method
    to print the list contents in sorted order without modifying
    the original list.
    """
    
    def print_sorted(self):
        """
        Print the list in sorted order (ascending).
        
        This method prints the elements of the list in ascending order
        without modifying the original list. All elements are assumed
        to be integers.
        """
        print(sorted(self))

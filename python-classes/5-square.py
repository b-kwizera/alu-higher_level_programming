#!/usr/bin/python3
"""This module defines a Square class with size validation, area calculation, and custom printing."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with an optional size.
        
        Args:
            size (int): Size of the square's sides (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square with validation.
        
        Args:
            value (int): New size to assign.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.
        
        Returns:
            int: Area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' characters. If size is 0, print an empty line."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

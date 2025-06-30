#!/usr/bin/python3
"""This module defines a Square class with size validation and area computation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with a given size (default is 0).
        
        Args:
            size (int): Size of the square's side.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # uses the setter for validation

    @property
    def size(self):
        """Get the size of the square.
        
        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.
        
        Args:
            value (int): New size to set.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
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

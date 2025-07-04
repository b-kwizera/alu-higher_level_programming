#!/usr/bin/python3
"""This module defines a Square class with size and position attributes."""


class Square:
    """Represents a square with size and position for printing."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position.

        Args:
            size (int): Size of the square sides (default is 0).
            position (tuple): Tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

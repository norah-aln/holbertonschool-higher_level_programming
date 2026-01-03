#!/usr/bin/python3
"""Module that defines a Square class with position"""


class Square:
    """Class that defines a square with position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size and position

        Args:
            size: The size of the square (default: 0)
            position: The position of the square (default: (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size attribute

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute with validation

        Args:
            value: The new size value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position attribute

        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute with validation

        Args:
            value: The new position value

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square (size * size)
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with # characters at the given position"""
        if self.__size == 0:
            print()
            return

        # Print vertical offset (position[1])
        for _ in range(self.__position[1]):
            print()

        # Print the square with horizontal offset (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

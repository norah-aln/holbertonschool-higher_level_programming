#!/usr/bin/env python3
"""Module that demonstrates duck typing with shapes"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape"""

    def __init__(self, radius):
        """Initialize a Circle with a radius

        Args:
            radius: The radius of the circle
        """
        self.radius = abs(radius)

    def area(self):
        """Calculate and return the area of the circle

        Returns:
            float: The area of the circle
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter of the circle

        Returns:
            float: The perimeter (circumference) of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle

        Returns:
            int/float: The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle

        Returns:
            int/float: The perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing

    Args:
        shape: An object that implements area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

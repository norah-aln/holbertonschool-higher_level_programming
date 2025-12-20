#!/usr/bin/env python3
"""Module that defines abstract Animal class and its subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal"""

    @abstractmethod
    def sound(self):
        """Abstract method that should return the sound of the animal"""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal"""

    def sound(self):
        """Returns the sound a dog makes

        Returns:
            str: The string "Bark"
        """
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal"""

    def sound(self):
        """Returns the sound a cat makes

        Returns:
            str: The string "Meow"
        """
        return "Meow"

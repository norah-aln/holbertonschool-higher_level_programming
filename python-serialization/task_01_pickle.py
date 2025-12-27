#!/usr/bin/env python3
"""Module for serializing custom objects using pickle"""
import pickle


class CustomObject:
    """Custom class with name, age, and student status"""

    def __init__(self, name, age, is_student):
        """Initialize CustomObject

        Args:
            name: Person's name (string)
            age: Person's age (integer)
            is_student: Student status (boolean)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes in formatted output"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle

        Args:
            filename: Name of the file to save the serialized object
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle

        Args:
            filename: Name of the file containing the serialized object

        Returns:
            CustomObject instance or None if error occurs
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None

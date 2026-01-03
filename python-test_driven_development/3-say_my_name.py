#!/usr/bin/python3
"""Module for printing names

This module provides a function to print a formatted name.
"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>

    Args:
        first_name: First name (must be string)
        last_name: Last name (must be string), defaults to empty string

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")

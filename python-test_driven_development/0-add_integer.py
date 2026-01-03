#!/usr/bin/python3
"""Module for adding two integers

This module provides a function to add two numbers (integers or floats)
and return the result as an integer.
"""


def add_integer(a, b=98):
    """Add two integers or floats and return an integer result

    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98

    Returns:
        The addition of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    if isinstance(a, float) and (a != a or a == float('inf') or a == float('-inf')):
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and (b != b or b == float('inf') or b == float('-inf')):
        raise ValueError("cannot convert float NaN to integer")
    
    return int(a) + int(b)

#!/usr/bin/python3
"""Module that checks if object is instance of or inherited from a class"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of or inherited from a_class

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if obj is instance of or inherited from a_class, False otherwise
    """
    return isinstance(obj, a_class)

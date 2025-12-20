#!/usr/bin/python3
"""Module that checks if object inherited from a class"""


def inherits_from(obj, a_class):
    """Returns True if obj inherited (directly or indirectly) from a_class

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if obj inherited from a_class, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

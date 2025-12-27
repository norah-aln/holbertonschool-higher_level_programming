#!/usr/bin/python3
"""Module that converts a JSON string to an object"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string

    Args:
        my_str: The JSON string to convert

    Returns:
        Python data structure represented by JSON string
    """
    return json.loads(my_str)

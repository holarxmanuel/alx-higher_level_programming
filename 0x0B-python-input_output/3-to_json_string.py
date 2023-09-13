#!/usr/bin/python3
"""
Defines a function to convert an object to a JSON representation as a string.
"""

import json


def to_json_string(my_obj):
    """
    Convert the provided object to its JSON representation as a string.

    :param my_obj: The object to be converted to JSON.
    :return: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)

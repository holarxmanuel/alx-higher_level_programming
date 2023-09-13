#!/usr/bin/python3
"""
Defines a function to convert a JSON string to a Python object.
"""


import json


def from_json_string(my_str):
    """
    Convert the provided JSON string to a Python object.

    :param my_str: The JSON string to be converted.
    :return: The Python object represented by the JSON string.
    """
    return json.loads(my_str)

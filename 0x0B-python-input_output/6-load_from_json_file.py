#!/usr/bin/python3
"""
Defines a function to load an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Load an object from the specified JSON file.

    :param filename: The name of the JSON file to load the object from.
    :return: The Python object loaded from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

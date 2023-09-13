#!/usr/bin/python3
"""
Defines a function to save an object to a text file in JSON format.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Serialize the object to a JSON representation and save it

    :param my_obj: The object to be serialized and saved.
    :param filename: The name of the file will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

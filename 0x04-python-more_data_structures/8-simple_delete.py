#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key from a dictionary.

    :param a_dictionary: The input dictionary
    :param key: The key to delete (default is empty string)
    :return: The updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

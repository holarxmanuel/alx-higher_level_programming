#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value in a dictionary.

    :param a_dictionary: The input dictionary
    :return: The key with the biggest integer value, or None if no score is found
    """
    if not a_dictionary:
        return None

    max_key = max(a_dictionary, key=a_dictionary.get)
    return max_key

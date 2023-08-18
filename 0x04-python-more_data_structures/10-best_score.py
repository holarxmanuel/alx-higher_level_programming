#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns the key with the highest integer value."""
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None

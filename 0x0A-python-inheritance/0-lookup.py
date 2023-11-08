#!/usr/bin/python3
"""
Module: 0-lookup

Description:
    A Python module that defines a function `lookup`
    which returns a list of
    available attributes and methods of an object.

"""


def lookup(obj):
    """Return the list of available
    attributes and methods of an object."""
    return dir(obj)

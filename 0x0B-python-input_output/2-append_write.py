#!/usr/bin/python3
"""
Defines a function to append text and count characters added.
"""


def append_write(filename="", text=""):

    """
    Append text to the specified filef ormat and return the character count.

    :param filename: The name of the file to append to.
    :param text: The text to append.
    :return: The number of characters added.
    """

    with open(filename, "a", encoding="utf-8") as file:
        chars_added = file.write(text)
    return chars_added

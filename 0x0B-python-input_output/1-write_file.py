#!/usr/bin/python3
"""
Defines a file-writing function.
"""


def write_file(filename="", text=""):
    """
    Write a string to a UTF-8 text file.

    :param filename: The name of the file to write.
    :param text: The text to write to the file.
    :return: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

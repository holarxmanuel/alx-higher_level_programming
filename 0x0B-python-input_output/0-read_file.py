#!/usr/bin/python3
"""
Text file reader script.
"""


def read_file(filename=""):
    """
    Print the content of a UTF-8 text file to stdout.

    :param filename: The name of the file to read (default: '').
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")


if __name__ == "__main__":
    read_file()

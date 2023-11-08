#!/usr/bin/python3
"""
Module: 1-my_list

Description:
    A Python module that defines a
    class MyList that inherits from list.
    It also provides a public instance
    method print_sorted that prints the list,
    sorted in ascending order.

"""


class MyList(list):
    """A class that inherits from list
    and provides additional functionality."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    pass

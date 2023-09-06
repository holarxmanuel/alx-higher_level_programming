#!/usr/bin/python3

"""
This is a module that contains a class that avoids
dynamically created attributes.
"""


class UniqueLockedClass:
    __slots__ = ['unique_first_name']

    def __init__(self):
        """Init method"""
        pass


if __name__ == "__main__":
    lc = UniqueLockedClass()
    lc.unique_first_name = "Alice"
    print(lc.unique_first_name)  # Allowed

    try:
        lc.unique_last_name = "Smith"  # Should raise AttributeError
    except AttributeError as e:
        print(e)

#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("An intentional type exception")
    except TypeError as e:
        return (e)

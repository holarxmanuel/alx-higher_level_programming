#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """
    Computes the square value of all integers in a matrix using map.

    :param matrix: 2-dimensional array
    :return: New matrix with squared values
    """
    return (list(map(lambda row: list(map(lambda x: x**2, row)), matrix)))

#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    :param matrix: A 2D array of integers
    :return: A new matrix with each value squared
    """
    squared_result = []
    for row in matrix:
        squared_row = list(map(lambda x: x**2, row))
        squared_result.append(squared_row)
    return squared_result

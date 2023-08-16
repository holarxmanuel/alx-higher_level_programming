#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, num in enumerate(row):
            if idx < len(row) - 1:
                print("{}".format(num), end=" ")
            else:
                print("{}".format(num), end="")
        print()

#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix to store squared values
    squared_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row for the squared values
        squared_row = []

        # Iterate through each element in the row
        for value in row:
            # Square the value and append it to the squared row
            squared_row.append(value ** 2)

        # Append the squared row to the squared matrix
        squared_matrix.append(squared_row)

    return squared_matrix

if __name__ == "__main__"
   

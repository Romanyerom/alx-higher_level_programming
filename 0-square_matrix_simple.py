#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    new_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row for the squared values
        new_row = []

        # Iterate through each element in the row and compute the square
        for element in row:
            squared_value = element ** 2
            new_row.append(squared_value)

        # Append the new row to the new matrix
        new_matrix.append(new_row)

    return (new_matrix)

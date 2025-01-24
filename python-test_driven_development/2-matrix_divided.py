#!/usr/bin/python3
"""
function divide the matrix by div
"""


def matrix_divided(matrix, div):
    """
    the function
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    return [[round(data / div, 2) for data in row] for row in matrix]

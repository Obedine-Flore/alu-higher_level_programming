#!/usr/bin/python3
"""This script efines a matrix division function."""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix."""
    if not isinstance(matrix, (list,)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    mat = []
    for i in range(len(matrix)):
        mat.append(list())
        for j in range(len(matrix[i])):
            mat[i].append(round(matrix[i][j] / div, 2))
    return mat

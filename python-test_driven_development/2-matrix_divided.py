#!/usr/bin/python3
"""
This function divides each element of a matrix
"""

def matrix_divided(matrix, div):
    """divides matrix by constant"""
    if not isinstance(matrix, (list,)):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers or floats")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix
                            (list of lists) of integers or floats")
        for element in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix
                                (list of lists) of integersor floats")
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix = []
    for i in range(len(matrix)):
        matrix.append(list())
        for j in range(len(matrix[i])):
            matrix[i].append(round(matrix[i][j] / div, 2))
    return matrix

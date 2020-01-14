#!/usr/bin/python3
"""
 This is the 2-matrix_divided module
 containing the matrix_divided function
 returns all elements of a matrix divided
"""


def matrix_divided(matrix, div):
    """
     matrix_divided function
    """
    mat_err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(mat_err)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix == [[]] or matrix == []:
        raise TypeError(mat_err)
    aux = matrix[0]
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(mat_err)
        if len(row) != len(aux):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(row, list):
            raise TypeError(mat_err)
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(mat_err)
    return [[round((x / div), 2) for x in row] for row in matrix]

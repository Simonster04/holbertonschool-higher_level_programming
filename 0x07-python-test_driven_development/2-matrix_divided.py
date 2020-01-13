#!/usr/bin/python3
def matrix_divided(matrix, div):
    return [[round((x / div), 2) for x in row] for row in matrix]

#!/usr/bin/python3
"""
 contains pascal_triangle function
"""


def pascal_triangle(n):
    """ returns a list of lists of integers
     representing the Pascals triangle of n """
    pascal = []
    if n <= 0:
        return pascal
    pascal.append([1])
    if n == 1:
        return pascal
    pascal.append([1, 1])
    if n == 2:
        return pascal
    for i in range(2, n):
        aux = []
        aux.append(1)
        aux2 = [pascal[i - 1][j] + pascal[i - 1][j + 1]\
            for j in range(len(pascal) - 1)]
        aux += aux2
        aux.append(1)
        pascal.append(aux)
    return pascal

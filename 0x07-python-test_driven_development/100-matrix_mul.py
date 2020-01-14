#!/usr/bin/python3
"""

 This module contains the matrix_mul function

"""


def matrix_mul(m_a, m_b):
    """
     this functions return the mul between two matrix 
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a == [[]] or m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == [[]] or m_b == []:
        raise ValueError("m_b can't be empty")
    for rowa in m_a:
        if not isinstance(rowa, list):
            raise TypeError("m_a must be a list of lists")
        for numa in rowa:
            if not isinstance(numa, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(m_a[0]) != len(rowa):
            raise TypeError("each row of m_a must be of the same size")
    for rowb in m_b:
        if not isinstance(rowb, list):
            raise TypeError("m_b must be a list of lists")
        for numb in rowb:
            if not isinstance(numb, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(m_b[0]) != len(rowb):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m_ab = [[0 for row in range(len(m_b[0]))] for col in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_ab[i][j] += m_a[i][k] * m_b[k][j]
    return m_ab

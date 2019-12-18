#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lena, lenb = len(tuple_a), len(tuple_b)
    sum_tuple = ((tuple_a[0] if lena >= 1 else 0) + (tuple_b[0] if lenb >= 1 else 0),
                (tuple_a[1] if lena >= 2 else 0) + (tuple_b[1] if lenb >= 2 else 0))
    return sum_tuple

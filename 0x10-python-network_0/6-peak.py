#!/usr/bin/python3
"""
 Contains find_peak function
"""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 0:
        return None
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    len_l = len(list_of_integers)
    low = len_l - (len_l - 1)
    high = len_l - 1
    return find_peak(list_of_integers[low:high])

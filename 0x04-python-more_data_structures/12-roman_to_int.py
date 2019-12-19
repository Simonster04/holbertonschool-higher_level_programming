#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    i = 0
    res = 0
    while i < len(roman_string):
        s1 = d[roman_string[i]]
        if (i + 1) < len(roman_string):
            s2 = d[roman_string[i + 1]]
            if s1 >= s2:
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res

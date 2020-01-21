#!/usr/bin/python3
"""
 contains number_of_lines function
"""


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """
    with open(filename, encoding="utf-8") as myFile:
        lines = 0
        while True:
            line = myFile.readline()
            lines += 1
            if not line:
                break
    return lines - 1

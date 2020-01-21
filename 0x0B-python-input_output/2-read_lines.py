#!/usr/bin/python3
"""
 contains read_ines function
"""


def read_lines(filename="", nb_lines=0):
    """ reads n lines of textfile-UTF8 and prints to stdout """
    with open(filename, encoding="utf-8") as myFile:
        if nb_lines == 0:
            print(myFile.read(), end="")
        for i in range(nb_lines):
            print(myFile.readline(), end="")

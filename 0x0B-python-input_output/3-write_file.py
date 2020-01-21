#!/usr/bin/python3
"""
 contains write_file function
"""


def write_file(filename="", text=""):
    """  writes a str to a textfile & return num of chars """
    with open (filename, encoding="utf-8", mode="w") as myFile:
        myFile.write(text)
        return len(text)

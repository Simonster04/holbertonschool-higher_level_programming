#!/usr/bin/python3
"""
 contains write_file function
"""


def write_file(filename="", text=""):
    """  writes a string to a text file (UTF8)
     and returns the number of characters written
    """
    with open (filename, encoding="utf-8", mode="w") as myFile:
        myFile.write(text)
        return len(text)

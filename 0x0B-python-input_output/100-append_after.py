#!/usr/bin/python3
"""
 Contains append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text after a specific string """
    with open(filename, encoding="utf-8") as myFile:
        linelist = []
        while True:
            line = myFile.readline()
            linelist.append(line)
            if search_string in line:
                linelist.append(new_string)
            if not line:
                break
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.writelines(linelist)

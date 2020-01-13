#!/usr/bin/python3
"""
 This module contains text_indentation function
"""


def text_indentation(text):
    """ 
     print a text with 2 new line after each . ? or :
    """
    aux = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print(i, end="")
            print()
            print()
            aux = 1 
        else:
            if aux == 0:
                print(i, end="")
            else:
                if i == ' ' or i == '\t':
                    pass
                else:
                    print(i, end="")
                    aux = 0

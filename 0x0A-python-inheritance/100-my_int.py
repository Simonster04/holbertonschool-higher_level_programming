#!/usr/bin/python3
"""
 contains MyInt class
"""


class MyInt(int):
    """ class MyInt that inherits from int """
    def __eq__(self, other):
        """ equal to notequal """
        return False

    def __ne__(self, other):
        """ not equal to equal """
        return True

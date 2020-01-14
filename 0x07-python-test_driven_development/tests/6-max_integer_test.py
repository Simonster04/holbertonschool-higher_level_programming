#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unit test class """
    def test_mod_docstr(self):
        """ test module docstring """
        mod = __import__("6-max_integer").__doc__
        self.assertTrue(len(mod) >1)

    def test_fun_docstr(self):
        """ test function docstring """
        fun = max_integer.__doc__
        self.assertTrue(len(fun) >1)

    def test_one_max(self):
        """ test normal args """
        self.asserEqual(max_integer[2, 4, 8], 8)

    def test_several_max(self):
        """ test several max """
        self.asserEqual(max_integer[2, 8, 8], 8)

    def test_no_max(self):
        """ Test no arguments """
        self.assertIsNone(max_integer())

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
if __name__ == __main__:
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    print("{:d} + {:d} = {:d}".format(a, b, add(a + b)))
    print("{:d} - {:d} = {:d}".format(a, b, add(a - b)))
    print("{:d} * {:d} = {:d}".format(a, b, add(a * b)))
    print("{:d} / {:d} = {:d}".format(a, b, add(a / b)))


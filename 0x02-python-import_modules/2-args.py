#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenav = len(argv)
    if lenav == 1:
        print("{:d} arguments.".format(lenav - 1))
    elif lenav == 2:
        print("{:d} argument:".format(lenav - 1))
    else:
        print("{:d} arguments:".format(lenav - 1))
    for i in range(lenav):
        if i < 1:
            continue
        print("{:d}: {:s}".format(i, argv[i]))

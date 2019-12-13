#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenav = len(argv)
    add = 0
    for i in range(lenav):
        if i < 1:
            continue
        add = add + int(argv[i])
    print("{:d}".format(add))

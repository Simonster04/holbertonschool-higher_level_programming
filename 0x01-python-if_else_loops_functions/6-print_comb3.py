#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if i != j and i < j:
            print("{:d}{:d}".format(i, j), end="")
            if i == 8 and j == 9:
               print()
            else:
               print(end=", ")

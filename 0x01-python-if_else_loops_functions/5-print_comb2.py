#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print("{:d}".format(0), end="")
    print("{:d}".format(i), end="")
    if i < 99:
        print(", ", end="")
print()

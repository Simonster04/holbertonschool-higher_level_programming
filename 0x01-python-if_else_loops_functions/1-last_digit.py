#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = abs(number) % 10
if number < 0:
    lastdig *= -1
if lastdig > 5:
    print("Last digit of %d is %d and is greater than 5" % (number, lastdig))
elif lastdig < 6 and lastdig != 0:
    print("Last digit of %d is %d and is less than 6 and not 0" % (number, lastdig))
else:
    print("Last digit of %d is %d and is 0" % (number, lastdig))

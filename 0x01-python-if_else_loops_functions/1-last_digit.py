#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = abs(number) % 10
if number < 0:
    lastd *= -1
if lastd > 5:
    print("Last digit of %d is %d and is greater than 5" % (number, lastd))
elif lastd < 6 and lastd != 0:
    print("Last digit of %d is %d and is less than 6 and not 0" % (number, lastd))
else:
    print("Last digit of %d is %d and is 0" % (number, lastd))

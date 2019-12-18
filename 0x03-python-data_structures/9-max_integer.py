#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    for i in range(len(my_list)):
        if i < 1:
            max = my_list[i]
        elif my_list[i] >= max:
            max = my_list[i]
    return max

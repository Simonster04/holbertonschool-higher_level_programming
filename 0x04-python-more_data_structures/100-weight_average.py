#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num, div = 0, 0
    for i in range(len(my_list)):
        num += my_list[i][0] * my_list[i][1]
        div += my_list[i][1]
    return num / div

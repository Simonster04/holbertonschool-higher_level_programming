#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            if type(my_list_1[i]) != int or type(my_list_2[i]) != int:
                print("wrong type")
                new_list.append(0)
            else:
                new_list.append(my_list_1[i] / my_list_2[i])
        return new_list
    except ZeroDivisionError:
        print("division by 0")
        new_list.append(0)
    finally:
        return new_list

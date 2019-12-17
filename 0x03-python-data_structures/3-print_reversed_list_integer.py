def print_reversed_list_integer(my_list=[]):
    str = "{}"
    my_list.reverse()
    for i in range(len(my_list)):
        print(str.format(my_list[i]))

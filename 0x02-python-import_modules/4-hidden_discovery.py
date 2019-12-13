#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    elem_hidden4 = dir(hidden_4)
    for s in elem_hidden4:
        if s[:2] == "__":
            continue
        else:
            print("{:s}".format(s))

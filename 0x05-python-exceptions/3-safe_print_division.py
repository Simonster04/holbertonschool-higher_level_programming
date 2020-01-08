#!/usr/bin/python3
def safe_print_division(a, b):
    div = 0
    try:
        if b == 0:
            div = None
        else:
            div = a / b
        return div
    except ZeroDivisionError:
        return None

    finally:
        print("Inside result: {}".format(div))

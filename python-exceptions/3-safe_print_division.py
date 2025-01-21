#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        azer = a / b
    except (ZeroDivisionError):
        azer = None
    finally:
        print("Inside result: {}".format(azer))
        return azer

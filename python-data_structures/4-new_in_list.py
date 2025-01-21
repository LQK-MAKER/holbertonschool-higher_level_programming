#!/usr/bin/python3
def new_in_list(my_list, idx, liste):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = liste
        return new_list

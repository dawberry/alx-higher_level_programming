#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    size = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            size += 1
        except TypeError:
            break
    print("")
    return size

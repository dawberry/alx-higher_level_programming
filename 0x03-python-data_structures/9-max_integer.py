#!/usr/bin/python3
def max_integer(my_list=[]):
    larg = my_list[0]
    for i in my_list:
        if i > larg:
            larg = i
    return larg


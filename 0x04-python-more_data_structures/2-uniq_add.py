#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    lis = set(my_list)
    for i in lis:
        sum += i
    return sum

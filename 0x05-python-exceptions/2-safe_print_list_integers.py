#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    size = 0
    for i in range(x):
        try:
            int(my_list[i])
            print("{}".format(my_list[i]), end="")
            size += 1
        except:
            i += 1
    print("")
    return size

lis = [1,2,34,5,9]
print("{}".format( safe_print_list_integers(lis, 3)))

lis = [1, 3, 4, "dave", 10]
print("{}".format(safe_print_list_integers(lis, 7)))

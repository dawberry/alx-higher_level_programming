#!/usr/bin/python3

def safe_print_integer(value):
    try:
        int(value)
        return value
    except ValueError:
        return "{} is not an integer".format(value)

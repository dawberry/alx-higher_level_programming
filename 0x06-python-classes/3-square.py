#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError
            elif size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self. __size ** 2

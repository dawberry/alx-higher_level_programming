#!/usr/bin/python3
"""Check Tyepe"""


class Square:
    """Private instance attribute: size"""

    def __init__(self, size=0):
        """Initalizes attribute size"""

        try:
            if not isinstance(size,  int):
                raise TypeError
            elif size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = size

#!/usr/bin/python3
"""Check Tyepe"""


class Square:
    """Private instance attribute: size"""

    def __init__(self, size=0):
        """Initalizes attribute size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

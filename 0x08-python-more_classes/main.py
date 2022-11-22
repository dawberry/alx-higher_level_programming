#!/usr/bin/python3

Rectangle = __import__("1-rectangle").Rectangle

new_rect = Rectangle()

print(new_rect.width)
new_rect.width = 20
print(new_rect.width)

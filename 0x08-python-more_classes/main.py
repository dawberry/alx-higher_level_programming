#!/usr/bin/python3

Rectangle = __import__("2-rectangle").Rectangle

new_rect = Rectangle()


new_rect.width = 20
new_rect.height = 15
print(new_rect.area())
print(new_rect.perimeter())

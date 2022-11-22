#!/usr/bin/python3

Rectangle = __import__("3-rectangle").Rectangle

new_rect = Rectangle()


new_rect.width = 4
new_rect.height = 2
print(new_rect.area())
print(new_rect.perimeter())

print(new_rect)

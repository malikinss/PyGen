'''
TODO:
    Write a program that calculates the value ⌈x⌉+⌊x⌋ given a real number x.
NOTE:
    ⌈x⌉ - the ceiling of the number
    ⌊x⌋ - the floor of the number
'''
from math import floor, ceil

x = float(input())

print(floor(x)+ceil(x))

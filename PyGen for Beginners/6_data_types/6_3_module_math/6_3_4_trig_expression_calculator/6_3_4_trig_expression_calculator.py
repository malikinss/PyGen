'''
TODO:
    Write a program that calculates the value of a trigonometric expression
    sinx+cosx+tan^2x for a given number of degrees x.

    Trigonometric functions take an argument in radians.

    To convert degrees to radians, use the formula:
        r = (x*pi)/180

    The math module contains a built-in radians() function that converts
    an angle from degrees to an angle in radians.
'''
from math import radians, sin, cos, tan

x = radians(float(input()))
f = sin(x) + cos(x) + tan(x)**2

print(f)

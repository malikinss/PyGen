'''
TODO:
    A polynomial of degree n is an expression of the form:
        a(n) * x^n + a(n-1) * x^(n-1) + ... + a(2) * x^2 + a(1) * x + a(0)
    where a(n), a(n-1), ..., a(2), a(1), a(0) are the coefficients of
    the polynomial (a(n) ≠ 0).

    The first line of the program input contains the coefficients of
    the polynomial, separated by a space, and an integer x on the second line.

    Write a program that calculates the value of the specified polynomial
    for a given value of x.

NOTE:
    The solution to the problem must be written as a function
    evaluate(coefficients, x), which accepts a list of coefficients and
    an argument value.

    The evaluate() function must be implemented based on the built-in map()
    and reduce() functions.
'''
from typing import Callable
from functools import reduce


# Define the lambda function for accumulating the polynomial value
accumulate: Callable = lambda acc, coef, x: acc * x + coef

# Lambda function to evaluate polynomial using Horner's method
evaluate: Callable = lambda coefficients, x: reduce(
    lambda acc, coef: accumulate(acc, coef, x), map(int, coefficients), 0
)

# Read input
coefficients = input().split()
x = int(input())

# Compute and print the polynomial result
print(evaluate(coefficients, x))

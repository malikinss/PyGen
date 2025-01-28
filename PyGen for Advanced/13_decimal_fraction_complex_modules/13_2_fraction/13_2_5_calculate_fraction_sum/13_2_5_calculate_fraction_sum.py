'''
TODO:
    The program is given a natural number n as input.

    Write a program that calculates and outputs a rational number equal to
    the value of the expression:
        1/(1^2) + 1/(2^2) + 1/(3^2) + 1/(4^2) + ... + 1/(n^2)
'''
from fractions import Fraction


def calculate_fraction_sum(n: int) -> Fraction:
    result_fraction = Fraction(1)

    for i in range(2, n+1):
        result_fraction += Fraction(1, i**2)

    return result_fraction


# Input: natural number n
n = int(input())

# Output: rational number equal to the value of the expression
print(calculate_fraction_sum(n))

'''
TODO:
    Given two natural numbers m and n.

    Write a program that reduces the fraction m / n and prints it.
'''
from fractions import Fraction


def reduce_fraction(m: int, n: int) -> Fraction:
    return Fraction(m, n)


# Input natural numbers m and n
m = int(input())
n = int(input())

# Call the function and print the reduced fraction
print(reduce_fraction(m, n))

'''
TODO:
    Dima is in the seventh grade and now they are learning about ordinary
    fractions with natural numerator and denominator.

    Yesterday in math class Dima learned that a fraction is called proper if
    its numerator is smaller than the denominator, or irreducible if there is
    no fraction equal to it with smaller natural numerator and denominator.

    Dima loves math, so at home he experimented for a long time, inventing and
    solving different problems with proper irreducible fractions.

    Dima suggests that you solve one of these problems using a computer.

    The program is given a natural number n as input.

    Write a program that finds the largest proper irreducible fraction with
    the sum of the numerator and denominator equal to n.

NOTE:
    You may need the gcd() function, which allows you to find the greatest
    common divisor (GCD) of two numbers.

    The function is implemented in the math module.
'''
from math import gcd


def largest_proper_irreducible_fraction(n: int):
    # Initialize an empty list to store proper irreducible fractions
    result_list = []

    # Iterate over possible numerators from 1 to n//2
    for numerator in range(1, n):
        denominator = n - numerator

        # Check if the fraction is proper and irreducible
        if numerator < denominator and gcd(numerator, denominator) == 1:
            result_list.append((numerator, denominator))

    # Find the fraction with the largest value
    max_fraction = max(result_list, key=lambda x: x[0] / x[1])

    return max_fraction


# Input: natural number n
n = int(input())

# Output: the largest proper irreducible fraction
numerator, denominator = largest_proper_irreducible_fraction(n)
print(f"{numerator}/{denominator}")

'''
TODO:
    The program is given a natural number n as input.

    Write a program that outputs, in ascending order, all irreducible
    fractions between 0 and 1 whose denominator does not exceed n.

NOTE:
    You may need the gcd() function, which allows you to find the greatest
    common divisor (GCD) of two numbers.

    The function is implemented in the math module.
'''
from math import gcd
from fractions import Fraction
from typing import List


def get_irreducible_fractions(max_denominator: int) -> List[Fraction]:
    """
    Get all irreducible fractions between 0 and 1 with denominators
    not exceeding the given maximum denominator.

    Args:
        max_denominator (int): The maximum denominator for the fractions.

    Returns:
        List[Fraction]: A list of irreducible fractions in ascending order.
    """
    fractions_list: List[Fraction] = []

    # Iterate over all possible denominators from 2 to max_denominator
    for denominator in range(2, max_denominator + 1):
        # Iterate over all possible numerators from 1 to denominator - 1
        for numerator in range(1, denominator):
            # Check if the numerator and denominator are coprime
            if gcd(numerator, denominator) == 1:
                # Add the fraction to the list
                fractions_list.append(Fraction(numerator, denominator))

    # Sort the fractions in ascending order
    sorted_fractions: List[Fraction] = sorted(fractions_list)
    return sorted_fractions


# Input the maximum denominator
max_denominator: int = int(input())

# Get and print the irreducible fractions
irreducible_fractions = get_irreducible_fractions(max_denominator)
print(*irreducible_fractions, sep='\n')

'''
TODO:
    Given two fractions in the format a/b, write a program that calculates
    and displays their sum, difference, product, and quotient.
'''
from fractions import Fraction


def calculate_fractions(fraction_1: str, fraction_2: str):
    frac_1 = Fraction(fraction_1)
    frac_2 = Fraction(fraction_2)

    print(f"{fraction_1} + {fraction_2} = {frac_1 + frac_2}")
    print(f"{fraction_1} - {fraction_2} = {frac_1 - frac_2}")
    print(f"{fraction_1} * {fraction_2} = {frac_1 * frac_2}")
    print(f"{fraction_1} / {fraction_2} = {frac_1 / frac_2}")


# Input fractions as strings
fraction_1 = input()
fraction_2 = input()

# Call the function to calculate and display the results
calculate_fractions(fraction_1, fraction_2)

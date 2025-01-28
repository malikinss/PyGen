'''
TODO:
    Decimal numbers separated by a space are stored in the string variable s.

    Complete the code so that it prints the sum of the largest and smallest
    numbers as a common fraction.
'''
from fractions import Fraction
from decimal import Decimal


def sum_of_max_and_min_as_fraction(s: str) -> Fraction:
    # Convert string of decimal numbers into Decimal objects
    numbers = [Decimal(element) for element in s.split()]

    # Find the maximum and minimum values
    max_number = max(numbers)
    min_number = min(numbers)

    # Calculate the sum of the max and min
    sum_max_min = max_number + min_number

    # Return the sum as a common fraction
    return Fraction(sum_max_min)


# Input string with decimal numbers
s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'

# Call the function and print the result
print(sum_of_max_and_min_as_fraction(s))

'''
TODO:
    The program receives two integers a and b as input.

    Write a program that prints:
        - the sum of numbers a and b;
        - difference between numbers a and b;
        - the product of numbers a and b;
        - quotient of numbers a and b;
        - the integer part of dividing the number a by b;
        - the remainder when dividing the number a by b;
        - square root of the sum of their 10th powers sqrt(a^10 + b^10)
'''
import math


def calculate_operations(a: int, b: int) -> None:
    """
    Performs various arithmetic operations on two integers and prints
    the results.

    The function computes and displays:
    1. Sum of a and b
    2. Difference between a and b
    3. Product of a and b
    4. Quotient of a divided by b
    5. Integer division of a by b
    6. Remainder of a divided by b
    7. Square root of the sum of a^10 and b^10

    Args:
        a (int): First integer input.
        b (int): Second integer input.

    Returns:
        None
    """
    # Sum
    sm = a + b
    print(sm)

    # Difference
    diff = a - b
    print(diff)

    # Product
    product = a * b
    print(product)

    # Quotient
    quotient = a / b
    print(quotient)

    # Integer division
    integer_division = a // b
    print(integer_division)

    # Remainder
    remainder = a % b
    print(remainder)

    # Square root of the sum of their 10th powers
    sqrt_sum_pow_10 = math.sqrt(a**10 + b**10)
    print(sqrt_sum_pow_10)


# Input
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Perform calculations
calculate_operations(a, b)

'''
TODO:
    The program is given a Decimal number d as input.

    Write a program that calculates the value of the expression:
        e^d + ln(d) + lg(d) + sqrt(d)
'''
from decimal import Decimal


def calculate_expression(decimal_number: Decimal) -> Decimal:
    """
    Calculates the value of the expression:
        e^d + ln(d) + lg(d) + sqrt(d).

    Args:
        decimal_number (Decimal): The input Decimal number.

    Returns:
        result (Decimal): The calculated value of the expression.
    """
    # Calculate each term of the expression
    exponential = decimal_number.exp()
    natural_log = decimal_number.ln()
    log_base_10 = decimal_number.log10()
    square_root = decimal_number.sqrt()

    # Sum the terms
    result = exponential + natural_log + log_base_10 + square_root

    return result


# Input and calculation
decimal_number = Decimal(input("Enter a decimal number: "))
print(
    f"The result of the expression is: {calculate_expression(decimal_number)}"
)

'''
TODO:
    Complete the given code so that it prints the sum of the largest and
    smallest digits of the Decimal number.
'''
from decimal import Decimal
from typing import Set


def get_digits_set(decimal_number: Decimal) -> Set[int]:
    """
    Extracts a set of all digits from a Decimal number, including 0 if the
    number is between -1 and 1.

    Args:
        decimal_number (Decimal): The Decimal number to process.

    Returns:
        digits_set (set): A set containing all unique digits of the number.
    """
    # Convert to a tuple representation
    number_tuple = decimal_number.as_tuple()

    # Extract all unique digits
    digits_set = set(number_tuple.digits)

    # If the number is between -1 and 1, ensure 0 is included in the digits set
    if -1 < decimal_number < 1:
        digits_set.add(0)

    return digits_set


# Input and main calculation
decimal_number = Decimal(input("Enter a decimal number: "))
digits_set = get_digits_set(decimal_number)

# Calculate and print the sum of the smallest and largest digits
print(
    f"The sum of the smallest and largest digits is:"
    f"{min(digits_set) + max(digits_set)}"
)

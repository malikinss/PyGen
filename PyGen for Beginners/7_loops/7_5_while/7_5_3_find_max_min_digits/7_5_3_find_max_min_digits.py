'''
TODO:
    Given a natural number n, (n≥10).

    Write a program that determines its maximum and minimum digits
'''


def find_max_min_digits(n: int) -> tuple:
    """
    Finds the maximum and minimum digits in a given natural number.

    Args:
        n (int): The number from which the digits are extracted.

    Returns:
        tuple: A tuple containing the maximum and minimum digits.
    """
    max_digit, min_digit = 0, 9

    while n > 0:
        last_digit = n % 10
        n //= 10

        max_digit = max(max_digit, last_digit)
        min_digit = min(min_digit, last_digit)

    return max_digit, min_digit


# Input
n = int(input("Enter a natural number (n ≥ 10): "))

# Output
max_digit, min_digit = find_max_min_digits(n)
print('Maximum digit is', max_digit)
print('Minimum digit is', min_digit)

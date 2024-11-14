'''
TODO:
    Given a natural number.

    Write a program that calculates:
        - the sum of its digits;
        - the number of digits in it;
        - multiplying its numbers;
        - the arithmetic mean of its digits;
        - its first digit;
        - the sum of its first and last digits.
'''


def calculate_number_properties(n: int):
    """
    Calculates the following properties of a given natural number:
    - The sum of its digits.
    - The number of digits in it.
    - The product of its digits.
    - The arithmetic mean of its digits.
    - Its first digit.
    - The sum of its first and last digits.

    Args:
        n (int): The natural number for which to calculate the properties.

    Returns:
        tuple: Contains the sum of digits, count of digits, product of digits,
               arithmetic mean, first digit, and the sum of first
               and last digits.
    """
    digit_sum = 0
    digit_cnt = 0
    digit_product = 1
    last_digit = n % 10
    first_digit = None

    while n > 0:
        cur_digit = n % 10
        if first_digit is None:
            first_digit = cur_digit  # Save the first digit
        digit_sum += cur_digit
        digit_cnt += 1
        digit_product *= cur_digit
        n //= 10

    digit_average = digit_sum / digit_cnt
    first_last_sum = first_digit + last_digit

    return digit_sum, digit_cnt, digit_product, digit_average, first_digit, first_last_sum


# Input
n = int(input("Enter a natural number: "))

# Calculate the properties
digit_sum, digit_cnt, digit_product, digit_average, first_digit, first_last_sum = calculate_number_properties(n)

# Output
print(digit_sum)
print(digit_cnt)
print(digit_product)
print(digit_average)
print(first_digit)
print(first_last_sum)

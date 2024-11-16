'''
TODO:
    Given a natural number.

    Write a program that calculates:
    - number of 3 digits in it;
    - how many times it contains the last digit;
    - the number of even digits;
    - the sum of its digits greater than five;
    - the result of multiplying digits greater than seven
    (if there are no digits greater than seven, then output 1,
    if there is only one such digit, then output it);
    - how many times it contains the numbers 0 and 5 (in total).
'''


def analyze_number(number: int) -> tuple[int, int, int, int, int, int]:
    """
    Analyzes a given natural number and returns multiple metrics:
    - Number of 3's in the number
    - How many times the last digit appears
    - Number of even digits
    - Sum of digits greater than five
    - Product of digits greater than seven (or 1 if no such digit)
    - Number of times 0 or 5 appear

    Args:
        number (int): The natural number to analyze.

    Returns:
        tuple[int, int, int, int, int, int]: A tuple containing the
        calculated values.
    """
    count_3 = 0
    last_digit = number % 10
    count_last_digit = 0
    count_even_digits = 0
    sum_greater_than_5 = 0
    product_greater_than_7 = 1
    count_0_5 = 0

    while number > 0:
        cur_digit = number % 10

        if cur_digit == 3:
            count_3 += 1

        if cur_digit == last_digit:
            count_last_digit += 1

        if cur_digit % 2 == 0:
            count_even_digits += 1

        if cur_digit > 5:
            sum_greater_than_5 += cur_digit

        if cur_digit > 7:
            product_greater_than_7 *= cur_digit

        if cur_digit == 0 or cur_digit == 5:
            count_0_5 += 1

        number //= 10

    # If no digit greater than 7 was found, set product to 1
    if product_greater_than_7 == 1 and cur_digit <= 7:
        product_greater_than_7 = 1

    return (count_3, count_last_digit, count_even_digits,
            sum_greater_than_5, product_greater_than_7, count_0_5)


# Input number
number = int(input("Enter a number: "))

# Call function and print the results
results = analyze_number(number)

for result in results:
    print(result)

'''
TODO:
    Write a program that uses the map() function to round all elements of
    the numbers list to 2 decimal places and then prints them, each on
    a separate line.
'''


def round_numbers(numbers: list) -> list:
    """
    Rounds all elements of the numbers list to 2 decimal places.

    Args:
        numbers (list): A list of floating-point numbers.

    Returns:
        list: A list of numbers rounded to 2 decimal places.
    """
    return list(map(round_until_to_decimal_simbols, numbers))


def round_until_to_decimal_simbols(number: float) -> float:
    """
    Rounds a number to 2 decimal places.

    Args:
        number (float): The number to round.

    Returns:
        float: The rounded number.
    """
    return round(number, 2)


numbers = [
    3.56773, 5.57668, 4.00914,
    56.24241, 9.01344, 32.12013,
    23.22222, 90.09873, 45.45,
    314.1528, 2.71828, 1.41546
]

# Call the function and print the results
rounded_numbers = round_numbers(numbers)
print(*rounded_numbers, sep='\n')

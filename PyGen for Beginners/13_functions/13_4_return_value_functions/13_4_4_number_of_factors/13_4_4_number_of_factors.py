'''
TODO:
    Write a function number_of_factors(num) that takes a number as an argument
    and returns the number of factors of that number.

NOTE:
    Use the already implemented get_factors(num) function from
    the previous task.
'''


def get_factors(num: int) -> list[int]:
    """
    Returns a list of all factors of a given natural number.

    A factor of a number is any integer that divides the number exactly
    without leaving a remainder. The function iterates through all integers
    from 1 to num and checks which ones divide num exactly.

    Args:
    num (int): A natural number whose factors are to be found.

    Returns:
    list[int]: A list of factors of the input number.
    """
    return [n for n in range(1, num + 1) if num % n == 0]


def number_of_factors(num: int) -> int:
    """
    Returns the number of factors of a given natural number.

    This function uses the get_factors function to find all factors and
    then returns the count of these factors.

    Args:
    num (int): A natural number whose number of factors is to be counted.

    Returns:
    int: The number of factors of the input number.
    """
    factors = get_factors(num)
    return len(factors)


# Example usage
n = int(input())  # Read input natural number

# Call the function and print the number of factors
print(number_of_factors(n))

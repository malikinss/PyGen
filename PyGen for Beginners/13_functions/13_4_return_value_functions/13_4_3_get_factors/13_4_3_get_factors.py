'''
TODO:
    Write a function get_factors(num) that takes a natural number
    as an argument and returns a list of all factors of that number.
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


# Example usage
n = int(input())  # Read input natural number
print(get_factors(n))  # Call the function and print the list of factors

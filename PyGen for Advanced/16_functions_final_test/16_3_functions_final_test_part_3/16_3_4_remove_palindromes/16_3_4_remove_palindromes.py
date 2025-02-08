'''
TODO:
    Given a list of integers numbers. Add code after the unpacking operator (*)
    to remove all palindromic numbers from the list and print the result on
    one line separated by a space.
'''


def remove_palindromes(numbers: list) -> None:
    """
    Removes all palindromic numbers from the given list and prints the
    remaining numbers on one line separated by a space.

    Parameters:
    - numbers (list): A list of integers.
    """
    filtered_numbers = list(filter(lambda x: str(x) != str(x)[::-1], numbers))
    print(*filtered_numbers)


# Example usage:
numbers = [
    18, 191, 9009, 5665,
    78, 77, 45, 23,
    19991, 908, 8976, 6565,
    5665, 10, 1000, 908,
    909, 232, 45654, 786
]
remove_palindromes(numbers)

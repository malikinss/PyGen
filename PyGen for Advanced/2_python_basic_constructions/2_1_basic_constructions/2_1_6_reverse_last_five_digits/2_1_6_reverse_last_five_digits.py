'''
TODO:
    Given a five-digit or six-digit natural number.

    Write a program that will reverse the order of its last five digits.
'''


def reverse_last_five_digits(n: int) -> int:
    """
    Reverses the order of the last five digits of a given number.

    Args:
        n (int): A five or six-digit natural number.

    Returns:
        int: The number with the last five digits reversed.
    """
    n_str = str(n)

    # If the number has more than five digits, reverse the last five
    if len(n_str) > 5:
        return int(n_str[:-5] + n_str[-5:][::-1])

    # If the number has exactly five digits, reverse all of them
    return int(n_str[::-1])


# Input
n = int(input())

# Output
print(reverse_last_five_digits(n))

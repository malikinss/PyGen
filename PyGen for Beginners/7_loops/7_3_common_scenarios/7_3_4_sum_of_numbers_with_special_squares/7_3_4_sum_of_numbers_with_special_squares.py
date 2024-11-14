'''
TODO:
    The input to the program is a natural number n.

    Write a program that calculates the sum of those numbers
    from 1 to n (inclusive) whose square ends in 2, 5, or 8.

    If there are no such numbers in the specified range, then output 0.
'''


def sum_of_numbers_with_special_squares(n: int) -> int:
    """
    Calculates the sum of numbers from 1 to n (inclusive) whose square
    ends in 2, 5, or 8.

    Args:
        n (int): The upper limit of the range.

    Returns:
        int: The sum of numbers whose square ends in 2, 5, or 8.
    """
    total = 0

    for i in range(1, n + 1):
        if (i ** 2) % 10 in [2, 5, 8]:
            total += i

    return total


# Input data
n = int(input("Enter a natural number n: "))

# Call the function and print the result
result = sum_of_numbers_with_special_squares(n)
print(result)

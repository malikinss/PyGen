'''
TODO:
    The input to the program is a natural number n.

    Write a program to calculate the alternating sum
    1 - 2 + 3 - 4 + 5 - 6 + ... + (-1)^(n+1) * n.
'''


def alternating_sum(n: int) -> int:
    """
    Calculates the alternating sum for the sequence:
        1 - 2 + 3 - 4 + 5 - 6 + ... + (-1)^(n+1) * n.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        int: The alternating sum of the sequence.
    """
    sum_result = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            sum_result += i  # Add odd numbers
        else:
            sum_result -= i  # Subtract even numbers

    return sum_result


# Input
n = int(input("Enter a natural number: "))

# Call the function and print the result
result = alternating_sum(n)
print(result)

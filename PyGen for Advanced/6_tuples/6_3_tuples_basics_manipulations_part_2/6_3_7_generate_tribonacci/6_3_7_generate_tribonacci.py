'''
TODO:
    Write a program that reads a natural number n and prints the first
    n numbers of the Tribonacci sequence.

    The Tribonacci sequence is a sequence of natural numbers where each
    subsequent number is the sum of the three previous ones:
        1,1,1,3,5,9,17,31,57,105, …
'''
from typing import List


def generate_tribonacci(n: int) -> List[int]:
    """
    Generates the first n numbers of the Tribonacci sequence.

    The Tribonacci sequence starts with 1, 1, 1 and each subsequent number
    is the sum of the previous three numbers.

    Args:
    n (int): The number of Tribonacci numbers to generate.

    Returns:
    List[int]: A list containing the first n numbers of
               the Tribonacci sequence.
    """
    # Initializing the first three numbers
    f1, f2, f3 = 1, 1, 1
    result = []

    # Generating the Tribonacci sequence
    for _ in range(n):
        result.append(f1)
        f1, f2, f3 = f2, f3, f1 + f2 + f3

    return result


# Input
n = int(input("Enter a natural number n: "))

# Generate and print the Tribonacci sequence
tribonacci_sequence = generate_tribonacci(n)
print(*tribonacci_sequence)

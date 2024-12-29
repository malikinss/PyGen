'''
TODO:
    Write a program to determine whether a number is the product
    of two numbers from a given set.

    The program should output the result as a “YES” or “NO” answer.

    The first line contains the number n (0<n<1000) - the number of numbers
    in the set.

    In the next n lines, the integers that make up the set (may be repeated)
    are entered.

    Then follows an integer, which is or is not the product of two numbers
    from the set.

NOTE:
    A number from a set cannot be multiplied by itself.
    In other words, the two factors must have different indexes in the set.
'''
from typing import List


def is_product_in_set(seq: List[int], target: int) -> str:
    """
    Determines if a number can be expressed as the product of two distinct
    numbers from a set.

    Parameters:
    - seq (List[int]): A list of integers representing the set.
    - target (int): The target number to check.

    Returns:
    - str: “YES” if the product exists, “NO” otherwise.
    """
    size = len(seq)

    for i in range(size):
        for j in range(size):
            if i != j and seq[i] * seq[j] == target:
                return "YES"

    return "NO"


def main() -> None:
    """
    Main function to handle input, process data, and output the result.
    """
    size = int(input("Enter the number of elements in the set: "))
    seq = [int(input("Enter element: ")) for _ in range(size)]
    target = int(input("Enter target number: "))

    result = is_product_in_set(seq, target)
    print(result)


if __name__ == "__main__":
    main()

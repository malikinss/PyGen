'''
TODO:
    The input to the program is a text string of natural numbers.

    A list of numbers is formed from it.

    Write a program to count the number of numbers that are greater than
    the number preceding them in this list.
'''
from typing import List


def count_greater_than_previous(numbers: List[int]) -> int:
    """
    Count the number of elements in the list that are greater than
    the preceding element.

    Parameters:
    - numbers (List[int]): A list of integers.

    Returns:
    - int: The count of elements greater than the previous one.
    """
    counter = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            counter += 1
    return counter


def main() -> None:
    """
    Main function to handle user input and print the results.
    """
    numbers = [int(n) for n in input("Enter a sequence of numbers: ").split()]
    result = count_greater_than_previous(numbers)
    print(result)


if __name__ == "__main__":
    main()

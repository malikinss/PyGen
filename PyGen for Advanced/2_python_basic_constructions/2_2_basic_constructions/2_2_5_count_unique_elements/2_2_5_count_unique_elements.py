'''
TODO:
    The input to the program is a string of text containing natural numbers
    arranged in non-decreasing order.

    A list of numbers is formed from the string.

    Write a program to count the number of different elements in a list.
'''
from typing import List


def count_unique_elements(numbers: List[str]) -> int:
    """
    Count the number of unique elements in a non-decreasing list of numbers.

    Parameters:
    - numbers (List[str]): A list of numbers as strings.

    Returns:
    - int: The number of unique elements in the list.
    """
    if not numbers:
        return 0  # Return 0 if list is empty

    counter = 1  # Start at 1 for the first unique element

    for i in range(len(numbers) - 1):
        if numbers[i] != numbers[i + 1]:
            counter += 1

    return counter


def main() -> None:
    """
    Main function to handle user input and print the count of unique elements.
    """
    numbers = input("Enter a sequence of non-decreasing numbers: ").split()
    result = count_unique_elements(numbers)
    print(result)


if __name__ == "__main__":
    main()

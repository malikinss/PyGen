'''
TODO:
    The input to the program is a text string of natural numbers.

    A list of numbers is formed from the elements of the string.

    Write a program that swaps the places of adjacent elements
    of a list (a[0] with a[1], a[2] with a[3], etc.).

    If there is an odd number of elements in the list, then the last
    one remains in its place.
'''
from typing import List


def swap_adjacent_elements(numbers: List[str]) -> List[str]:
    """
    Swap adjacent elements in a list. If the list has an odd number
    of elements, the last element remains unchanged.

    Parameters:
    - numbers (List[str]): A list of numbers as strings.

    Returns:
    - List[str]: A list with adjacent elements swapped.
    """
    for i in range(0, len(numbers) - 1, 2):
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers


def main() -> None:
    """
    Main function to handle user input and print the swapped list.
    """
    numbers = input("Enter a sequence of numbers: ").split()
    result = swap_adjacent_elements(numbers)
    print(*result)


if __name__ == "__main__":
    main()

'''
TODO:
    The input to the program is a text string of natural numbers.

    A list of numbers is formed from the elements of the string.

    Write a program to cyclically shift the elements of a list to the right,
    with the last element becoming the first and the rest moving one position
    forward, towards increasing indices.
'''
from typing import List


def cyclic_shift_right(numbers: List[str]) -> List[str]:
    """
    Perform a cyclic shift of the elements in a list to the right.
    The last element becomes the first, and the rest shift one
    position forward.

    Parameters:
    - numbers (List[str]): A list of numbers as strings.

    Returns:
    - List[str]: A list with cyclically shifted elements.
    """
    if not numbers:
        return numbers  # Return empty list if input is empty

    return [numbers[-1]] + numbers[:-1]


def main() -> None:
    """
    Main function to handle user input and print the cyclically shifted list.
    """
    seq = input("Enter a sequence of numbers: ").split()
    result = cyclic_shift_right(seq)
    print(*result)


if __name__ == "__main__":
    main()

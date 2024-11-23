'''
TODO:
    The input to the program is a natural number n, and then n strings.

    Write a program that creates a list from the given strings and
    prints it out.
'''
from typing import List


def create_string_list(n: int) -> List[str]:
    """
    This function takes an integer n and returns a list of n strings entered
    by the user.

    Parameters:
    n (int): The number of strings to input.

    Returns:
    List[str]: A list of n strings.
    """
    lst = []
    for i in range(n):
        lst.append(input(f"Enter string {i+1}: "))
    return lst


# Get the number of strings to be entered
n = int(input("Enter the number of strings: "))

# Call the function and store the result in lst
lst = create_string_list(n)

# Print the resulting list
print(lst)

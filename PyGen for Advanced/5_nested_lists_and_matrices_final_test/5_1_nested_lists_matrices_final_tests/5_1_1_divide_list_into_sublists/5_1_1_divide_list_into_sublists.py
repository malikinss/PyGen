'''
TODO:
    The program is given a text string containing characters and a number n
    as input.

    A list is formed from this string.

    Write a program that divides the list into nested sublists so that n
    consecutive elements belong to different sublists.
'''
from typing import List


def divide_list_into_sublists(
    input_list: List[str], n: int
) -> List[List[str]]:
    """
    Divides a list into nested sublists such that n consecutive elements
    belong to different sublists.

    Args:
        input_list (List[str]): List of elements to divide.
        n (int): Number of sublists to divide the list into.

    Returns:
        List[List[str]]: Nested list with divided sublists.
    """
    number_of_elem = len(input_list)
    result_list: List = [[] for _ in range(n)]  # Initialize n empty sublists

    # Distribute elements into sublists
    for i in range(n):
        for j in range(i, number_of_elem, n):
            result_list[i].append(input_list[j])

    return result_list


def main() -> None:
    """
    Main function to take user input, divide the list, and print the result.
    """
    # Read the input string and split it into a list
    input_list = input("Enter a list of elements (space-separated): ").split()

    # Read the number of sublists to divide into
    n = int(input("Enter the number of sublists: "))

    # Divide the list and print the result
    result = divide_list_into_sublists(input_list, n)
    print(result)


if __name__ == "__main__":
    main()

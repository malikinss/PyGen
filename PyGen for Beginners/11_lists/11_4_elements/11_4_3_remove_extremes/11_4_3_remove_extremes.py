'''
TODO:
    When analyzing data collected as part of a scientific experiment,
    it can be useful to remove the largest and smallest value.

    The input to the program is a natural number n, and then n different
    natural numbers.

    Write a program that removes the smallest and largest values from given
    numbers, and then prints the remaining numbers each on a separate line
    without changing their order.
'''


def remove_extremes(numbers: list[int]) -> list[int]:
    """
    Removes the smallest and largest values from a list of numbers.

    Args:
        numbers (list[int]): List of natural numbers.

    Returns:
        list[int]: The list after removing the smallest and largest values.
    """
    max_num, min_num = max(numbers), min(numbers)
    return [num for num in numbers if num != max_num and num != min_num]


# Input: number of integers and their values
n = int(input("Enter the number of integers: "))
numbers = [int(input("Enter a number: ")) for _ in range(n)]

# Remove the smallest and largest numbers and display the remaining numbers
remaining_numbers = remove_extremes(numbers)
print(*remaining_numbers, sep='\n')

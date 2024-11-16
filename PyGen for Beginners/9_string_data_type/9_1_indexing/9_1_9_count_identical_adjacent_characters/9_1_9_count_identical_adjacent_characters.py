'''
TODO:
    The input to the program is one line.

    Write a program that determines how many identical adjacent
    characters are in it.
'''


def count_identical_adjacent_characters(input_string: str) -> int:
    """
    Counts the number of identical adjacent characters in the input string.

    Args:
        input_string (str): The string to be analyzed.

    Returns:
        int: The count of identical adjacent characters.
    """
    count = 0

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1

    return count


# User input
given_string = input("Enter a string: ")

# Call function and print the result
print(count_identical_adjacent_characters(given_string))

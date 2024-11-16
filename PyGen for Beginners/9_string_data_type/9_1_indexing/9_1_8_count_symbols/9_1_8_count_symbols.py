'''
TODO:
    The input to the program is one line.

    Write a program that determines how many times + and * occur in a string.
'''


def count_symbols(input_string: str) -> None:
    """
    Counts the occurrences of '+' and '*' in the input string and prints
    the results.

    Args:
        input_string (str): The string to be analyzed.

    Returns:
        None: Prints the counts of '+' and '*'.
    """
    cnt_plus = input_string.count("+")
    cnt_mul = input_string.count("*")

    print("Symbol + occurs", cnt_plus, "times")
    print("Symbol * occurs", cnt_mul, "times")


# User input
given_string = input("Enter a string: ")

# Count and display results
count_symbols(given_string)

'''
TODO:
    The input to the program is a line of text in which the letter "h"
    occurs at least twice.

    Write a program that removes the first and last occurrences
    of the letter "h" from this string, as well as all characters between them.
'''


def remove_h_between(s):
    """
    Removes the first and last occurrences of 'h' from the string,
    along with all characters between them.

    Args:
    s (str): The input string containing at least two 'h' characters.

    Returns:
    str: The modified string after removing the first and last 'h'
    and everything in between.
    """
    first = s.find("h")
    last = s.rfind("h")

    # Remove the part between the first and last 'h', including the 'h's
    result = s[:first] + s[last+1:]

    return result


# Read the input string
given_string = input()

# Call the function and print the result
print(remove_h_between(given_string))

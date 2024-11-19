'''
TODO:
    The input to the program is two numbers a and b.

    Write a program that, for each code value in the range a
    through b (inclusive), outputs its corresponding character
    from the Unicode character table.
'''


def unicode_range_to_chars(a: int, b: int):
    """
    Converts each Unicode code point in the given range to its
    corresponding character.

    Args:
        a (int): The starting Unicode code point.
        b (int): The ending Unicode code point.

    Returns:
        None: Prints the characters corresponding to the code points
        in the range.
    """
    for i in range(a, b + 1):
        print(chr(i), end=' ')


# Input the two numbers a and b from the user
a = int(input())
b = int(input())

# Call the function
unicode_range_to_chars(a, b)

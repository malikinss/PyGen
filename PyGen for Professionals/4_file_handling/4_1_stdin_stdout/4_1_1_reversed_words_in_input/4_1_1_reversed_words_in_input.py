'''
TODO:
    Write a program that takes an arbitrary number of lines and puts all the
    characters in reverse order on each line input.

NOTE:
    The order in which lines are output must match the order in which they
    were entered.

    If the program receives nothing as input, then it should output nothing.
'''
import sys


def reversed_words_in_input():
    """
    Reads multiple lines from the standard input, reverses the characters on
    each line, and outputs them in the same order.

    The function does the following:
        1. Reads the input lines from standard input.
        2. Reverses the characters of each line.
        3. Outputs the reversed lines in the same order they were input.

    If no input is provided, the function outputs nothing.

    Input:
        - Lines of text from standard input.

    Output:
        - Each line of text with characters reversed, printed to standard
          output.
    """
    data = list(map(str.strip, sys.stdin))

    for row in data:
        reversed_row = row[-1::-1] + '\n'
        sys.stdout.writelines(reversed_row)


reversed_words_in_input()

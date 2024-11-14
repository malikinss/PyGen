'''
TODO:
    The input to the program is a sequence of words,
    each word on a separate line.

    The end of the sequence is the word "END" or "end" (capital
    or small letters, no quotes).

    At the same time, the words “END” and “end” themselves are not
    included in the sequence, only symbolizing its end.

    Write a program that prints the terms of a given sequence.
'''


def print_sequence_until_keywords(keywords=None) -> None:
    """
    Reads a sequence of words from the user, stopping when any keyword
    in 'keywords' is entered.
    Prints each word in the sequence on a new line, excluding
    the keyword(s) themselves.

    Args:
        keywords (set of str, optional): Set of keywords indicating
        the end of input.
        Defaults to {'END', 'end'}.
    """
    if keywords is None:
        keywords = {'END', 'end'}

    while True:
        given_word = input("Enter a word (type 'END' or 'end' to stop): ")
        if given_word in keywords:
            break
        print(given_word)


# Call the function
print_sequence_until_keywords()

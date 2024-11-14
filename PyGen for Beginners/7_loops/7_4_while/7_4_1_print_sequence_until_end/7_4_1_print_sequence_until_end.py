'''
TODO:
    The input to the program is a sequence of words, each word
    on a separate line.

    The end of the sequence is the word "END" (without quotes).

    At the same time, the word "END" itself is not included in the sequence,
    only symbolizing its end.

    Write a program that prints the terms of a given sequence.
'''


def print_sequence_until_end() -> None:
    """
    Reads a sequence of words from the user, stopping when
    the word "END" is entered.

    Prints each word in the sequence on a new line, excluding "END" itself.
    """
    while True:
        given_word = input("Enter a word (or 'END' to stop): ")
        if given_word == "END":
            break
        print(given_word)


# Call the function
print_sequence_until_end()

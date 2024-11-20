'''
TODO:
    The program is fed with 3 different words as input.
    You need to sort these words in ascending lexicographic order and output
    them on one line, separated by a space character.
'''


def sort_words_lexicographically(words_num: int) -> None:
    """
    Reads a specified number of words from input, sorts them in
    lexicographic order, and prints them on a single line
    separated by a space.

    Parameters:
    words_num (int): The number of words to be read from the user.
    """
    # Using list comprehension to read 'words_num' words
    words = [input() for _ in range(words_num)]

    # Sorting the words in lexicographic order
    sorted_words = sorted(words)

    # Output the sorted words on one line, separated by spaces
    print(*sorted_words)


# Calling the function with 3 words as input
sort_words_lexicographically(3)

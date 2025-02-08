'''
TODO:
    The gematria of a word is the sum of the numerical values of its letters.

    To calculate the gematria of a word in this problem:
        1) convert the word to uppercase;
        2) calculate the numerical value of the letter as
           code(letter) - code(letter A);

    The program is given a natural number n as input, and then n lines
    of English words in different registers.

    Write a program that outputs words in the initial register
    (each on a separate line) in ascending order of their gematria.

    If the gematria of the words matches, they are output in alphabetical
    (lexicographic) order.

NOTE:
    To get the code of a character, use the built-in function ord().

    Words in the input data may be repeated.
'''


def gematria(word: str) -> tuple[int, str]:
    """
    Calculates the gematria of a word.

    Parameters:
    - word (str): The word whose gematria is to be calculated.

    Returns:
    - tuple: A tuple containing the gematria value and the original word.
    """
    return sum(ord(c.upper()) - ord('A') for c in word), word


def sort_words_by_gematria(n: int) -> None:
    """
    Sorts a list of words first by their gematria values in ascending order,
    and then alphabetically in case of ties.

    Parameters:
    - n (int): The number of words to be inputted.

    Returns:
    - None: This function prints the sorted words.
    """
    words = [input() for _ in range(n)]
    sorted_words = sorted(words, key=gematria)
    print(*sorted_words, sep='\n')


# Example usage
n = int(input())  # Number of words
sort_words_by_gematria(n)

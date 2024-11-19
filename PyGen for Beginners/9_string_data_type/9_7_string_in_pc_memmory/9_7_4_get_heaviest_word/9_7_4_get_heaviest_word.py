'''
TODO:
    By "heaviness" of a word we mean the sum of codes according to the Unicode
    table of all symbols of this word.

    Write a program that accepts 4 words and finds the heaviest word
    among them.

    If there are several heaviest words, then the program should output
    the first of them.
'''


def get_word_weight(word: str) -> int:
    """
    This function calculates the 'heaviness' of a word, which is the sum
    of the Unicode values of all characters in the word.

    Parameters:
    - word (str): The word for which the heaviness is calculated.

    Returns:
    - int: The total sum of Unicode values of the characters in the word.
    """
    return sum(ord(letter) for letter in word)


def get_heaviest_word(word1: str, word2: str, word3: str, word4: str) -> str:
    """
    This function finds the heaviest word among the four given words
    by comparing their 'heaviness', which is the sum of the Unicode
    values of their characters.

    Parameters:
    - word1 (str): The first word to compare.
    - word2 (str): The second word to compare.
    - word3 (str): The third word to compare.
    - word4 (str): The fourth word to compare.

    Returns:
    - str: The word with the highest 'heaviness'. If there are ties,
    the first word is returned.
    """
    words = [word1, word2, word3, word4]
    word_weights = [get_word_weight(word) for word in words]

    max_weight = max(word_weights)
    heaviest_index = word_weights.index(max_weight)
    return words[heaviest_index]


# Input words
word1 = input()
word2 = input()
word3 = input()
word4 = input()

# Find the heaviest word
heaviest_word = get_heaviest_word(word1, word2, word3, word4)

# Output the heaviest word
print(heaviest_word)

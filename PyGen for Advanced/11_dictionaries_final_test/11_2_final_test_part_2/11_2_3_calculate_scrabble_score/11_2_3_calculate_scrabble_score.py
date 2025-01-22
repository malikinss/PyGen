'''
TODO:
    In Scrabble, each letter is worth a certain number of points.

    The total value of a word is the sum of the points of its letters.

    The rarer a letter is, the more valuable it is:
        1 - A, E, I, L, N, O, R, S, T, U
        2 - D, G
        3 - B, C, M, P
        4 - F, H, V, W, Y
        5 - K
        8 - J, X
        10 - Q, Z
    Write a program to calculate the total value of the entered word.
'''


def calculate_scrabble_score(word: str) -> int:
    """
    Calculates the total Scrabble score for the given word.

    Args:
        word (str): The word for which to calculate the score.

    Returns:
        int: The total Scrabble score.
    """
    letter_price = {
        1: "AEILNORSTU",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ"
    }

    # Create a dictionary mapping each letter to its score
    price_mapping = {
        letter: score
        for score, letters in letter_price.items()
        for letter in letters
    }

    # Calculate total price by summing the score of each letter in the word
    total_price = sum(price_mapping.get(letter.upper(), 0) for letter in word)
    return total_price


# Example usage:
given_word = input("Enter a word: ").strip()
word_score = calculate_scrabble_score(given_word)
print(word_score)

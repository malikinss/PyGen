'''
TODO:
    It is necessary to write a program that implements the algorithm for
    writing this song.

    The algorithm displays the next letter in alphabetical order at the end of
    the sentence if it occurs in a line of text, and displays the next line
    without this letter.

NOTE:
    If there are no Tails, then you need to output the number 0.
'''


def process_string(word: str) -> None:
    """
    Removes letters from the Russian alphabet in alphabetical order
    from the input string and prints the updated string after each removal.

    Parameters:
    - word (str): The input string where letters are to be removed.

    Outputs:
    - The updated string and the letter removed at each step.
    """
    alpha = [chr(i) for i in range(1072, 1104)]  # Russian lowercase letters

    for letter in alpha:
        if letter in word:
            print(word, letter)  # Print the string with the current letter

            # Remove the letter
            word = word.replace(letter, '').replace('  ', ' ').strip()


# Example usage
word = input()
process_string(word)

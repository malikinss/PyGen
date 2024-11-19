'''
TODO:
    The program receives a letter of the Russian alphabet in upper case
    as input.

    Find the letter following it and display it on the screen.

    If the entered letter is the last in the alphabet, then display the text:
        "There are no further letters" (without quotes).

NOTE:
    Let's assume that the letter Ё is not in the Russian alphabet. 🤫
'''


def next_russian_letter(given_letter: str):
    """
    Given a Russian uppercase letter, finds the next letter
    in the Russian alphabet.

    If the given letter is the last one in the alphabet, it informs the user.

    Args:
        given_letter (str): A single uppercase Russian letter.

    Returns:
        None: Prints the next letter or a message if it's the last one.
    """
    # Unicode value for 'А' and 'Я' in the Russian alphabet
    last_letter_unicode = ord('Я')

    # Get the Unicode value of the given letter
    given_unicode = ord(given_letter)

    # Check if the given letter is the last in the alphabet
    if given_unicode == last_letter_unicode:
        print("There are no further letters")
    else:
        # Get the Unicode value of the next letter
        next_unicode = given_unicode + 1
        print(chr(next_unicode))


# Input the letter
given_letter = input()

# Call the function
next_russian_letter(given_letter)

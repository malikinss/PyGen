"""
TODO:
    Write a program to decrypt the secret word using frequency analysis.

NOTE:
    It is guaranteed that the letter frequencies do not repeat.
"""

from typing import Dict


def get_letters_dict(number_records: int) -> Dict[str, int]:
    """
    Reads the letters and their repetition rates from the input and creates
    a dictionary.

    Args:
        number_records (int): The number of letter-repetition pairs to input.

    Returns:
        Dict[str, int]: A dictionary where keys are letters and values
                        are their repetition rates.
    """
    letters_dict = {}
    for _ in range(number_records):
        msg = "Enter letter and repetition rate (e.g., A: 3): "
        letter, repetition_rate = input(msg).split(': ')
        letters_dict[letter] = int(repetition_rate)
    return letters_dict


def get_flipped_dict(given_dict: Dict[str, int]) -> Dict[int, str]:
    """
    Flips the keys and values of a dictionary.

    Args:
        given_dict (Dict[str, int]): The original dictionary.

    Returns:
        Dict[int, str]: The flipped dictionary with keys and values swapped.
    """
    return {value: key for key, value in given_dict.items()}


def get_decrypted_string(
    encrypted_string: str, letters_dict: Dict[str, int]
) -> str:
    """
    Decrypts an encrypted string using frequency analysis.

    Args:
        encrypted_string (str): The encrypted string.
        letters_dict (Dict[str, int]): A dictionary mapping letters
                                       to repetition rates.

    Returns:
        str: The decrypted string.
    """
    flipped_letters_dict = get_flipped_dict(letters_dict)
    decrypted_string = ''.join(
        flipped_letters_dict[encrypted_string.count(char)]
        for char in encrypted_string
    )
    return decrypted_string


# Input and decryption process
encrypted_string = input("Enter the encrypted string: ")
dictionary_letters_number = int(input("Enter the number of letters: "))
letters_dict = get_letters_dict(dictionary_letters_number)
decrypted_string = get_decrypted_string(encrypted_string, letters_dict)

print("Decrypted string:", decrypted_string)

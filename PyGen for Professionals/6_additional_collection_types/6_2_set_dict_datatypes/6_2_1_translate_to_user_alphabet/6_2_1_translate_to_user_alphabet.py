'''
TODO:
    Given a string of correspondence to the Latin alphabet: the first
    character of the string corresponds to the letter a, the second to b,
    the third to c, and so on.

    Each character corresponds to both uppercase and lowercase letters.
    The number of characters in the string matches the number of letters
    in the Latin alphabet.

    Write a program that uses this string to translate the given text.

    The first line of the program's input is a string of correspondence to
    the Latin alphabet, and the next line is the text to be translated.

    The program must use this string of correspondence to the
    Latin alphabet to translate the input text and output the result.

NOTE:
    The program must ignore all characters that are not Latin letters.
'''
from typing import Dict
from string import ascii_lowercase


def get_user_alphabet() -> Dict[str, str]:
    """
    Reads user-provided alphabet correspondence and constructs a translation
    dictionary.

    Returns:
        Dict[str, str]: A mapping of lowercase Latin letters to
        the user-defined alphabet.
    """
    user_mapping = input().strip()

    if len(user_mapping) < len(ascii_lowercase):
        raise ValueError("The provided alphabet mapping is incomplete.")

    return {
        letter: user_mapping[i] for i, letter in enumerate(ascii_lowercase)
    }


def translate_text(translation_map: Dict[str, str], text: str) -> str:
    """
    Translates the given text using the provided translation mapping.

    Args:
        translation_map (Dict[str, str]): Mapping of Latin letters to custom
        characters.
        text (str): Input text to be translated.

    Returns:
        str: The translated text.
    """
    translated_text = [
        translation_map[char.lower()].upper()
        if char.isupper() else translation_map.get(char, char)
        for char in text
    ]
    return ''.join(translated_text)


def main():
    """
    Reads input, constructs the translation dictionary, translates the text,
    and prints the result.
    """
    try:
        user_alphabet = get_user_alphabet()
        text_to_translate = input().strip()
        print(translate_text(user_alphabet, text_to_translate))
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

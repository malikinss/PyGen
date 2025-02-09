'''
TODO:
    Transliteration is the transfer of signs of one writing system by signs of
    another writing system, in which each sign (or sequence of signs) one
    writing system is transmitted by the corresponding sign (or sequence of
    signs) of another writing  system.

    A text file is available to you cyrillic.txt containing the text.

    Write a program to transliterate this file, that is, replace Cyrillic
    characters with Latin ones in accordance with the proposed table.

    All other symbols must be left unchanged.

    The result of the transliteration must be written to a file
    transliteration.txt .

NOTE:
    Consider that the executable program and the specified files are in the
    same folder.
'''

from typing import TextIO

# Transliteration dictionary to map Cyrillic characters to Latin equivalents
TRANSLITERATION_DICT = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g',
    'д': 'd', 'е': 'e', 'ё': 'jo', 'ж': 'zh',
    'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k',
    'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
    'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
    'ч': 'ch', 'ш': 'sh', 'щ': 'shh', 'ъ': '*',
    'ы': 'y', 'ь': "'", 'э': 'je', 'ю': 'ju', 'я': 'ya'
}


def transliterate_text(input_file: TextIO, output_file: TextIO) -> None:
    """
    Transliterates the content of a given file from Cyrillic to Latin based on
    a predefined dictionary.

    Args:
        input_file (TextIO): The input file object containing Cyrillic
                              text to be transliterated.
        output_file (TextIO): The output file object where the
                               transliterated text will be written.

    This function reads each character from the input file, replaces Cyrillic
    characters with their Latin equivalents, and writes the result to the
    output file.

    Characters not found in the transliteration dictionary are left unchanged.
    """
    for char in input_file.read():
        lower_char = char.lower()

        if char in TRANSLITERATION_DICT:
            output_file.write(TRANSLITERATION_DICT[char])
        elif lower_char in TRANSLITERATION_DICT:
            output_file.write(TRANSLITERATION_DICT[lower_char].capitalize())
        else:
            output_file.write(char)


def process_transliteration() -> None:
    """
    Reads a text file with Cyrillic text, transliterates it to Latin
    characters, and writes the result to a new file.

    This function opens the input file 'cyrillic.txt' and the output file
    'transliteration.txt'. It calls the `transliterate_text` function
    to process the content of the input file and writes the result to the
    output file.
    """
    with open('cyrillic.txt', 'r', encoding='utf-8') as input_file, \
         open('transliteration.txt', 'w', encoding='utf-8') as output_file:
        transliterate_text(input_file, output_file)


# Run the transliteration process
process_transliteration()

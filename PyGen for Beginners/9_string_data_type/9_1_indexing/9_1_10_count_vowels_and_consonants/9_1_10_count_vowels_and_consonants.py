'''
TODO:
    The input to the program is one string with the letters
    of the Russian language.

    Write a program that determines the number of vowels and consonants.
'''


def count_vowels_and_consonants(input_string: str) -> None:
    """
    Determines the number of vowels and consonants in a given string of
    Russian letters.

    Args:
        input_string (str): The string to be analyzed, consisting of
        Russian letters.

    Returns:
        None: Prints the counts of vowels and consonants.
    """
    vowels = 'аеёийоуюэяAEЁИЙОУЭЯ'
    consonants = 'бвгдеёжзийклмнопрстфхцчшщБВГДЕЁЖЗИЙКЛМНОПРСТФХЦЧШЩ'

    vowels_cnt = 0
    consonants_cnt = 0

    for char in input_string:
        if char in vowels:
            vowels_cnt += 1
        elif char in consonants:
            consonants_cnt += 1

    print('The number of vowels is', vowels_cnt)
    print('The number of consonants is', consonants_cnt)


# User input
given_string = input("Enter a string: ")

# Call function to count vowels and consonants
count_vowels_and_consonants(given_string)

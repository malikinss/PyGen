'''
TODO:
    You have a program that adds the fifth letter of each word in the food
    list to the list fifth.

    If a word does not have a fifth letter, the _ character is assumed to be
    that letter.

    Add a try-except construct to the code below to ensure that it runs
    without errors.
'''
from typing import List


def extract_fifth_letters(food: List[str]) -> List[str]:
    """
    Adds the fifth letter of each word in the food list to the fifth list.

    If a word does not have a fifth letter, the '_' character is assumed to
    be that letter.

    Args:
        food (List[str]): A list of food words.

    Returns:
        List[str]: A list containing the fifth letter of each word, or '_' if
        the word is too short.
    """
    fifth = []

    for x in food:
        try:
            letter_to_add = x[4]  # Fifth letter
        except IndexError:
            letter_to_add = '_'  # Default to '_' if the word is too short

        fifth.append(letter_to_add)

    return fifth


food = [
    'chocolate', 'chicken', 'corn',
    'sandwich', 'soup', 'potatoes',
    'beef', 'lox', 'lemonade'
]

result = extract_fifth_letters(food)
print(result)

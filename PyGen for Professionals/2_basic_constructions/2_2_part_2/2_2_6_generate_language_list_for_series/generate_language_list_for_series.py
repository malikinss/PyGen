'''
TODO:
    It is often impossible to translate TV shows without losing their original
    meaning, especially due to word games.

    A crazy director wants to make a series in which, for experimental
    purposes, he would use as many languages as possible to enjoy the beauty
    of each of them.

    Nevertheless, if you use too many languages, then the series will become
    incomprehensible to absolutely everyone, so the director gets random
    people on the street and asks them what languages they know, so he will
    use languages that all of them know.

    Write a program that determines which languages will be used in the series.

    The program should display a list of languages for the series in
    lexicographic order.

NOTE:
    If such a list cannot be compiled, it is necessary to print the text:
        The series will not be filmed
'''
from typing import List, Set


def get_set_of_languages() -> Set[str]:
    """
    Gets a set of languages from user input.

    Returns:
        Set[str]: A set of languages entered by the user.
    """
    return set(input().split(', '))


def get_persons_languages(number: int) -> List[Set[str]]:
    """
    Gets the languages each person knows.

    Args:
        number (int): The number of people.

    Returns:
        List[Set[str]]: A list of sets, where each set represents the
                        languages a person knows.
    """
    return [get_set_of_languages() for _ in range(number)]


def generate_language_list_for_series(number: int) -> str:
    """
    Generates the list of common languages for the series.

    Args:
        number (int): The number of people.

    Returns:
        str: A string of common languages in lexicographic order, or a message
             indicating the series won't be filmed.
    """
    languages_per_person = get_persons_languages(number)

    series_languages = set.intersection(*languages_per_person)

    if not series_languages:
        return 'The series will not be filmed'

    sorted_languages = sorted(series_languages)
    return ', '.join(sorted_languages)


# Take user input and print the result
number_of_people = int(input("Enter the number of people: "))
result = generate_language_list_for_series(number_of_people)
print(result)

'''
TODO:
    Write a function get_month(language, number), which takes as input
    two arguments language - language ru or en and number - month number
    (from 1 to 12) and returns the name of the month in Russian or English.
'''


def get_month(language: str, number: int) -> str:
    """
    Returns the name of the month based on the given language and month number.

    Args:
        language (str): The language in which the month name is to be returned.
        It can be 'ru' for Russian or 'eng' for English.
        number (int): The month number (from 1 to 12).

    Returns:
        str: The name of the month in the specified language.
    """
    # Russian month names
    month_ru = [
        'январь', 'февраль', 'март',
        'апрель', 'май', 'июнь',
        'июль', 'август', 'сентябрь',
        'октябрь', 'ноябрь', 'декабрь'
    ]

    # English month names
    month_eng = [
        'january', 'february', 'march',
        'april', 'may', 'june',
        'july', 'august', 'september',
        'october', 'november', 'december'
    ]

    # Select the appropriate month name based on language and number
    if language == 'ru':
        month_name = month_ru[number - 1]
    elif language == 'eng':
        month_name = month_eng[number - 1]

    return month_name


# Input
language = input("Enter language (ru or eng): ")
number_of_month = int(input("Enter month number (1-12): "))

# Output
print(get_month(language, number_of_month))

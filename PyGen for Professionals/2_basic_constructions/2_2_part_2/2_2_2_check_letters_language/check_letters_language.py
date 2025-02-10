'''
TODO:
    There are letters in Russian and English that look the same.

    Here is a list of English letters “AaBCcEeHKMOoPpTXxy”, and here are their
    Russian analogues "АаВСсЕеНКМОоРрТХху".

    Write a program that, for three letters from given lists of letters,
    determines whether they are Russian, English, or both (a mixture of
    Russian and English letters).

    The program should output:
        - ru - if all three letters are Russian
        - en - if all three letters are English
        - mix - if the letters include both Russian and English

NOTE:
    It is guaranteed that the three letters entered are in the set
    "AaBCcEeHKMOoPpTXxy" + "АаВСсЕеНКМОоРрТХху" (English + Russian letters).
'''


def check_letters_language(letters: str) -> str:
    """
    Determines the language of three letters (Russian, English, or both).

    Args:
        letters (str): Three letters from the set
                       "AaBCcEeHKMOoPpTXxy" + "АаВСсЕеНКМОоРрТХху"

    Returns:
        str: 'ru' if all three letters are Russian,
             'en' if all three letters are English,
             'mix' if a mixture of Russian and English letters.
    """
    russian_letters = 'АаВСсЕеНКМОоРрТХху'
    english_letters = 'AaBCcEeHKMOoPpTXxy'

    # Check if all three letters are Russian or English
    if all(letter in russian_letters for letter in letters):
        return 'ru'
    elif all(letter in english_letters for letter in letters):
        return 'en'
    else:
        return 'mix'

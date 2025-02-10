'''
TODO:
    Implement the choose_plural() function, which takes two arguments in the
    following order:
        - amount — natural number, quantity
        - declensions — a tuple of three declension variants of a noun

    The function should return a string obtained by combining a suitable noun
    from the declensions tuple and the amount amount, in the following format:
        <quantity> <noun>

NOTE:
    The tuple passed to the function is easy to make according to the mnemonic
    rule:
        one, two, five.
'''
from typing import Tuple


def choose_plural(amount: int, declensions: Tuple[str, str, str]) -> str:
    """
    Returns the correctly declined form of a noun based on the quantity.

    Args:
        amount (int): The quantity (natural number).
        declensions (Tuple[str, str, str]): A tuple of three declension
                                            variants of a noun: (singular,
                                            genitive singular, genitive plural)

    Returns:
        str: A string combining the quantity and the suitable noun form.

    Notes:
        The function uses a rule where:
            - one: nominative singular (declensions[0]),
            - two, three, four: genitive singular (declensions[1]),
            - others: genitive plural (declensions[2]).
    """
    nouns = {1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 0: 2}

    last_digit = amount % 10
    last_two_digits = amount % 100

    if 11 <= last_two_digits <= 19:
        return f"{amount} {declensions[2]}"

    return f"{amount} {declensions[nouns[last_digit]]}"

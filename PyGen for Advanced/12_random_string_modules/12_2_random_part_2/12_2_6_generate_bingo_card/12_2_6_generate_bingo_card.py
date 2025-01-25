'''
TODO:
    To play bingo, you need a 5*5 card containing different (unique) integers
    from 1 to 75 (inclusive), with the central cell empty (it is filled with
    the number 0).

    Lotto game "Super Bingo". Play the lottery online for free

    Write a program that uses the random module to generate and display
    a random card for playing bingo.

NOTE:
    For clarity, we recommend that you allocate exactly 3 characters for
    displaying each number.

    To do this, use the string method ljust().

    An example of a possible answer:
        1 16 31 46 61
        10 30 42 47 68
        3 18 0 48 63
        9 19 34 49 70
        5 20 35 50 65

    Other ways to generate a card for playing bingo are also possible.
'''
import random


def generate_bingo_card() -> list[str]:
    """
    Generates a random Bingo card with unique numbers between 1 and 75,
    with the center cell being empty (0).

    Returns:
        list[str]: A list of strings representing the Bingo card.
    """
    new_card: set = set()

    # Generate unique random numbers for the Bingo card
    while len(new_card) < 24:
        generated_number = str(random.randint(1, 75))
        new_card.add(generated_number.ljust(3))  # Ensure 3-character width

    # Convert set to list and insert 0 in the center (12th position)
    new_card_lst = list(new_card)
    new_card_lst.insert(12, '0  ')

    return new_card_lst


def print_bingo_card(card: list[str]) -> None:
    """
    Prints the Bingo card in a 5x5 grid format.

    Args:
        card (list[str]): A list representing the Bingo card.
    """
    for i in range(0, 25, 5):
        print(*card[i:i+5])


# Example usage
card = generate_bingo_card()
print_bingo_card(card)

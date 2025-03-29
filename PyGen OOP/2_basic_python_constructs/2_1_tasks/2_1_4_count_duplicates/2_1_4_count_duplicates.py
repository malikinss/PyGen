'''
TODO:
        Arthur has a small collection of Pokemon cards, some of which
        are duplicates.
        He wants to keep one card of each type and sell the rest.

        Write a program that determines how many duplicates Arthur can
        sell from his collection.

        Input:
            The program receives an arbitrary number of lines
            representing a collection of Pokemon cards.
            Each line contains the name of a Pokemon from the card.

        Output:
            The program should output a single number — the number of
            cards that can be sold from this collection to keep one card
            of each type.
'''
import sys


def read_input() -> list[str]:
    """
    Reads input from stdin and returns a list of stripped lines.

    Returns:
        list[str]: A list of Pokemon card names.
    """
    return [line.strip() for line in sys.stdin.readlines()]


def count_duplicates(cards: list[str]) -> int:
    """
    Counts the number of duplicate Pokemon cards.

    Args:
        cards (list[str]): A list of Pokemon card names.

    Returns:
        int: The number of duplicate cards.
    """
    return len(cards) - len(set(cards))


if __name__ == "__main__":
    given_cards = read_input()
    print(count_duplicates(given_cards))

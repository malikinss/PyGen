'''
TODO:
    Timur is making a shopping list, but since the number pad on his
    keyboard stopped working, instead of specifying the quantity of an
    item as a number, he adds it to the list as many times as he plans
    to buy.

    Timur writes all the items in lowercase, separated by commas.

    Write a program that outputs all the items from this shopping list,
    indicating the quantity for each.

    The program is given a sequence of items, separated by a comma
    without spaces.

    The program should output all the items entered, indicating for each
    one how many times it appears in this sequence.

    The items should be arranged in lexicographic order, each on a
    separate line, in the following format:
        <item>: <quantity>
'''
from collections import Counter


def parse_shopping_list() -> Counter[str]:
    """
    Reads the user input, splits it into individual items, and counts the
    occurrences of each item.

    Returns:
        Counter[str]: A Counter object containing the count of each item.
    """
    return Counter(input().split(','))


def print_shopping_list(item_counts: Counter[str]) -> None:
    """
    Prints the shopping list items and their quantities in lexicographic order.

    Args:
        item_counts (Counter[str]): A Counter object containing the count
        of each item.
    """
    for item, amount in sorted(item_counts.items()):
        print(f'{item}: {amount}')


print_shopping_list(parse_shopping_list())

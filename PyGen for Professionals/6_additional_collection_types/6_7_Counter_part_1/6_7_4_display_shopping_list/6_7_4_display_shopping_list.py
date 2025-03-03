'''
TODO:
    Timur lives in a world where the price of a product is determined as
    the sum of the Unicode codes of the letters of its name.

    The letter designation of this currency is two capital Latin
    letters UC.

    For example, a pen in his world costs:
    112 + 101 + 110 = 323UC

    Timur makes a shopping list, but since the block with numbers on his
    keyboard stopped working, instead of indicating the quantity of goods
    by number, he adds them to the list as many times as he plans to buy.

    Timur writes all the goods in lower case, separated by commas.

    Write a program that groups identical goods from this shopping list
    and determines the cost of each group.

    The program receives a sequence of goods separated by a comma without
    spaces as input.

    The program should group identical goods, determine the total cost of
    each group and output the result.

    The products must be in lexicographic order, each on a separate line,
    in the following format:
        <product>:
        <unit price> UC x <number of products in group> =
        <total cost of group> UC

NOTE:
    The program must add the required number of spaces if the product name
    is shorter than the others.

    You can get the Unicode code of a character using the ord() function.
'''
from collections import Counter


def get_item_counts() -> Counter[str]:
    """
    Reads the user input, splits it into individual items, and counts the
    occurrences of each item.

    Returns:
        Counter[str]: A Counter object containing the count of each item.
    """
    return Counter(input().split(','))


def calculate_item_price(item: str) -> int:
    """
    Calculates the price of an item based on the sum of Unicode values of its
    letters.

    Args:
        item (str): The name of the item.

    Returns:
        int: The price of the item.
    """
    return sum(map(ord, item))


def display_shopping_list(item_counts: Counter[str]) -> None:
    """
    Prints the shopping list items and their quantities in lexicographic order.

    Args:
        item_counts (Counter[str]): A Counter object containing the count
        of each item.
    """
    max_length = max(map(len, item_counts))

    for item, amount in sorted(item_counts.items()):
        unit_price = calculate_item_price(item)
        total_price = unit_price * amount
        print(
            f"{item.ljust(max_length)}: "
            f"{unit_price} UC x {amount} = {total_price} UC"
        )


if __name__ == "__main__":
    display_shopping_list(get_item_counts())

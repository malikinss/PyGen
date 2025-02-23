"""
TODO:
    After McDonald's left Russia, Timur decided to open his own small burger
    joint.

    The price of each burger in his restaurant is determined by the number of
    ingredients that the customer chooses.

    You have access to dictionaries in which the ingredient name is specified
    as the key, and its price is specified as the value.

    All ingredients are divided into categories, for example, vegetables are
    contained in one dictionary, sauces in another.

    Write a program that takes as input the ingredients selected by the
    customer and determines their total cost.

    The program receives as input a sequence of ingredients separated by a
    comma without spaces.

    The program should determine the total cost of the ingredients entered and
    output the result as a receipt listing the ingredients in lexicographic
    order, the quantity of each, and their total cost, in the following format:
        <ingredient 1> x <quantity 1>
        <ingredient 2> x <quantity 2>
        ...
        ------------------------------
        TOTAL: <total cost>p

NOTE:
    The program should add the required number of spaces if one ingredient is
    shorter than the others.

    The length of the dotted line should be equal to the length of the longest
    line in the receipt, including the line with the total cost.

    It is guaranteed that all ingredients selected by the visitor are present
    in the dictionaries.
"""
from typing import Dict, List
from collections import ChainMap, Counter


def get_max_string_length(strings: List[str]) -> int:
    """
    Returns the maximum string length from a list of strings.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        int: The length of the longest string.
    """
    return max(len(string) for string in strings)


def calculate_total_price(order: Counter,
                          total_ingredients: Dict[str, int]) -> int:
    """
    Calculates the total price of the order based on the selected ingredients.

    Args:
        order (Counter): A counter object containing the ingredients and their
        quantities.
        total_ingredients (Dict[str, int]): A dictionary with ingredient
        prices.

    Returns:
        int: The total price of the order.
    """
    price = 0
    for ingredient, amount in order.items():
        price += total_ingredients[ingredient] * amount
    return price


def generate_line(size: int) -> str:
    """
    Generates a line of dashes of a given size.

    Args:
        size (int): The length of the line.

    Returns:
        str: A string containing dashes.
    """
    return ''.ljust(size, '-')


def create_receipt(order: Counter) -> List[str]:
    """
    Prepares the receipt lines based on the order.

    Args:
        order (Counter): A counter object containing the ingredients and their
        quantities.

    Returns:
        List[str]: A list of strings representing the receipt.
    """
    total_price = calculate_total_price(order, total_ingredients)
    sorted_order = sorted(order)
    max_name_len = get_max_string_length(order.keys())

    receipt = [f'{ingredient.ljust(max_name_len)} x {order[ingredient]}' for ingredient in sorted_order]
    receipt.append(f'ИТОГ: {total_price}р')

    line_size = max(len(receipt[0]), len(receipt[-1]))
    receipt.insert(-1, generate_line(line_size))

    return receipt


def print_receipt(order: Counter) -> None:
    """
    Prints the receipt to the console.

    Args:
        order (Counter): A counter object containing the ingredients and their
        quantities.
    """
    receipt = create_receipt(order)
    for row in receipt:
        print(row)


# Ingredient prices
bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

# Combining all ingredient dictionaries
total_ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)

# Taking input from the user and counting the ingredients
order = Counter(input().split(','))

# Printing the receipt
print_receipt(order)

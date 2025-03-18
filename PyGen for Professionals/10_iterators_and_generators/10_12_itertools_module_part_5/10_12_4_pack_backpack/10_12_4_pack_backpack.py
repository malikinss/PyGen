'''
TODO:
    You have access to the items list, which contains a set of items.

    Each item is presented as a named tuple and has three parameters:
        - name
        - weight (in grams)
        - value (in rubles).

    There is also a backpack of a certain carrying capacity.

    Write a program that determines which items from the presented set should
    be taken to assemble a backpack with the maximum value of items inside,
    while observing the weight limit of the backpack.

    The first line of the program's input is a number - the carrying capacity
    of the backpack (in grams).

    The program should determine which items from the presented set should be
    taken to assemble a backpack with the maximum value of items inside, while
    observing the weight limit of the backpack, and output the names of the
    resulting items in lexicographic order, each on a separate line.

    If the backpack does not allow you to take any items, the program should
    output the text:
        The backpack cannot be assembled

NOTE:
    The backpack does not necessarily have to be completely full.
'''
from collections import namedtuple
from typing import List, Union
from itertools import combinations

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [
    Item('Обручальное кольцо', 7, 49_000),
    Item('Мобильный телефон', 200, 110_000),
    Item('Ноутбук', 2000, 150_000),
    Item('Ручка Паркер', 20, 37_000),
    Item('Статуэтка Оскар', 4000, 28_000),
    Item('Наушники', 150, 11_000),
    Item('Гитара', 1500, 32_000),
    Item('Золотая монета', 8, 140_000),
    Item('Фотоаппарат', 720, 79_000),
    Item('Лимитированные кроссовки', 300, 80_000)
]


def has_capacity(combination: List[Item], capacity: int) -> bool:
    """
    Checks if the total weight of the given combination of items does not
    exceed the backpack's capacity.

    Args:
        combination (List[Item]): The combination of items to check.
        capacity (int): The carrying capacity of the backpack in grams.

    Returns:
        bool: True if the total weight of the combination is within the
        capacity, False otherwise.
    """
    return sum(item.mass for item in combination) <= capacity


def pack_backpack(
    items: List[Item],
    capacity: int
) -> Union[List[str], List[str]]:
    """
    Determines which items from the presented set should be taken to assemble
    a backpack with the maximum value of items inside, while observing the
    weight limit of the backpack.

    Args:
        items (List[Item]): A list of available items to choose from.
                            Each item is represented as a named tuple
                            with 'name', 'mass', and 'price'.
        capacity (int): The maximum weight the backpack can carry, in grams.

    Returns:
        Union[List[str], List[str]]: A list of names of the selected items,
                                     sorted lexicographically, or a message
                                     stating that the backpack cannot be
                                     assembled if no valid combination is
                                     found.
    """
    best_combination = None
    max_value = 0

    for i in range(1, len(items) + 1):
        for comb in combinations(items, r=i):
            if has_capacity(comb, capacity):
                current_value = sum(item.price for item in comb)
                if current_value > max_value:
                    max_value = current_value
                    best_combination = comb

    if best_combination is None:
        return ["Рюкзак собрать не удастся"]

    best_combination_names = sorted(item.name for item in best_combination)
    return best_combination_names


print(*pack_backpack(items, int(input())), sep='\n')

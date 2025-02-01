'''
TODO:
    Write a function print_products() that takes an arbitrary number of
    arguments and prints a list of products (any non-empty string) like this:
        <product number>) <product name>
    (products are numbered starting with one).

    If there are no products among the arguments passed, the text No products
    should be printed.

NOTE:
    Note that the function should not take a list, but an arbitrary number
    of arguments.

    Numbers, lists, tuples, dictionaries, sets, and other non-string objects
    are not products and should be ignored.

    Note that the print_products() function should print the desired value,
    not return it.
'''
from typing import Any


def print_products(*args: Any) -> None:
    """
    Prints a numbered list of products among the provided arguments.

    A product is defined as any non-empty string.

    Non-string arguments, empty strings, and other types are ignored.

    Products are numbered starting from 1.

    If no products are found, prints "No products".

    Args:
        *args (Any): An arbitrary number of arguments.
    """
    counter: int = 0

    for element in args:
        if isinstance(element, str) and len(element) > 0:
            counter += 1
            print(f"{counter}) {element}")

    if counter == 0:
        print("No products")

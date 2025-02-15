'''
TODO:
    November has come and many stores have started sales, but as many people
    know, often discounted products are more expensive than without it.

    You have access to the sales.csv file, which contains pricing data for
    various household appliances.

    The first column contains the product name, the second column contains the
    old price, and the third column contains the new discounted price:
        name;old_price;new_price
        Built-in dishwasher De'Longhi DDW 06S;23089;31862
        Falmec Afrodite 60/600 hood;27694;18001
        ...

    Write a program that displays the names of those products whose prices
    have decreased.

    The products must be in their original order, each on a separate line.

NOTE:
    The delimiter in the sales.csv file is a semicolon, and quotation marks
    are not used.
'''
import csv
from typing import List, Tuple


def read_csv_data(filename: str) -> List[Tuple[str, int, int]]:
    """
    Reads product pricing data from a CSV file.

    Args:
        filename (str): The name of the CSV file.

    Returns:
        List[Tuple[str, int, int]]: A list of tuples where each tuple contains
        the product name, old price, and new price.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)  # Skip header row
        return [(row[0], int(row[1]), int(row[2])) for row in reader]


def display_discounted_products(products: List[Tuple[str, int, int]]) -> None:
    """
    Prints the names of products whose prices have decreased.

    Args:
        products (List[Tuple[str, int, int]]): A list of tuples containing
        product name, old price, and new price.

    Returns:
        None
    """
    for name, old_price, new_price in products:
        if new_price < old_price:
            print(name)


filename = 'sales.csv'
products_data = read_csv_data(filename)
display_discounted_products(products_data)

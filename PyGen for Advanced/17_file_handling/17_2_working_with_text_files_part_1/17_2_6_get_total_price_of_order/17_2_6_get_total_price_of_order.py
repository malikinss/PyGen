'''
TODO:
    You have access to the text file 'prices.txt' with information about the
    order from the online store.

    In it, each line is divided into three columns using the tab character(\t):
        1. product name;
        2. the quantity of the product (integer);
        3. the price (in rubles) of the product for 1 piece (integer).

    Write a program that displays the total cost of the order.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''
from typing import List


# Type alias for readability
OrderData = List[str]


def get_data_from_file(file_name: str) -> OrderData:
    """
    Reads data from a file and returns a list of lines.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - OrderData: A list of lines from the file.
    """
    with open(file_name, 'r', encoding='utf-8') as given_file:
        # Strip trailing whitespace and newline characters
        return [line.rstrip() for line in given_file]


def get_total_price_of_order(order_list: OrderData) -> int:
    """
    Calculates the total price of the order.

    Parameters:
    - order_list (OrderData): A list of strings containing product data.

    Returns:
    - int: The total cost of the order.
    """
    parsed_data = (line.split('\t') for line in order_list)

    return sum(int(qty) * int(price) for product, qty, price in parsed_data)


# Read data from file
data: OrderData = get_data_from_file('prices.txt')

# Print result
print(get_total_price_of_order(data))

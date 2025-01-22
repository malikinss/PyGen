'''
TODO:
    Write a program to count the number of units of each type of product
    purchased by each customer in an online store.

    The input to the program is the number n - the number of rows in
    the online store sales database.

    Then follow n rows with records of the type buyer product quantity, where
    buyer is the name of the buyer (a string without spaces), product is
    the name of the product (a string without spaces), quantity is the number
    of units of the product purchased (a natural number).

    The program should output a list of all buyers in lexicographic order,
    with a colon after each buyer's name, then a list of the names of all
    the products purchased by them in lexicographic order, with the number
    of units of the product after the name of each product.

    Information about each product is output on a separate line.
'''
from typing import Dict


def process_sale(
    client_name: str,
    sold_item: str,
    sold_amount: int,
    sales_per_client: Dict[str, Dict[str, int]]
) -> None:
    """
    Processes a single sale by updating the sales database for the given
    client and item.

    Args:
        client_name (str): The name of the client making the purchase.
        sold_item (str): The name of the product being purchased.
        sold_amount (int): The number of units of the product purchased.
        sales_per_client (Dict[str, Dict[str, int]]): The dictionary holding
                                                      the sales information.

    Returns:
        None
    """
    if client_name not in sales_per_client:
        sales_per_client[client_name] = {sold_item: sold_amount}
    elif sold_item not in sales_per_client[client_name]:
        sales_per_client[client_name][sold_item] = sold_amount
    else:
        sales_per_client[client_name][sold_item] += sold_amount


def print_sales_summary(sales_per_client: Dict[str, Dict[str, int]]) -> None:
    """
    Prints the sales summary for all clients, sorted by client names and
    product names.

    Args:
        sales_per_client (Dict[str, Dict[str, int]]): The dictionary holding
                                                      the sales information.

    Returns:
        None
    """
    for client, sale in sorted(sales_per_client.items()):
        print(client + ':')
        for item, amount in sorted(sale.items()):
            print(f"{item} {amount}")


def process_sales(number_of_sales: int) -> None:
    """
    Processes multiple sales and prints the sales summary.

    Args:
        number_of_sales (int): The number of sales to be processed.

    Returns:
        None
    """
    sales_per_client: Dict = {}

    for _ in range(number_of_sales):
        given_sale = input().split()
        client_name = given_sale[0]
        sold_item = given_sale[1]
        sold_amount = int(given_sale[2])

        process_sale(client_name, sold_item, sold_amount, sales_per_client)

    print_sales_summary(sales_per_client)


# Start the process by calling the function
number_of_sales = int(input())
process_sales(number_of_sales)

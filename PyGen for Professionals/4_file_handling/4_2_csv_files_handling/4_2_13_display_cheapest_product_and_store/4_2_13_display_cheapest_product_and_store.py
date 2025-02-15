'''
TODO:
    Dima really wants to eat, but he doesn't have much money.

    Help him determine the cheapest product and the store where it is sold.

    You have access to the prices.csv file, which contains information
    about the prices of products in various stores.

    The first column contains the name of the store, and the following
    columns contain the price of the corresponding product in this store:
        Shop;Cottage cheese;Buckwheat;Rice;Borodinsky bread;Apples;etc..
        Pyaterochka;69;133;129;83;141;90;72;123;149;89;88;106;54;84
        Magnet;102;87;95;75;109;112;97;82;101;134;69;61;141;79
        ...

    Write a program that determines and displays the cheapest product and
    the name of the store where it is sold, in the following format:
        <product name>: <store name>

    If there are several the cheapest goods, then you should output the
    goods whose name is lower in the lexicographic comparison.

    If one product is sold in several stores at one minimum price, then
    you should output the store whose name is lower in the lexicographic
    comparison.

NOTE:
    The separator in the prices.csv file is a semicolon, and quotation
    marks are not used.

    Example of output:
        Strawberry yogurt: VkusVill

    When opening the file, use an explicit indication of the UTF-8
    encoding.
'''
import csv
from typing import List, Dict, Tuple

INPUT_FILE: str = 'prices.csv'


def read_csv(filename: str, delimiter: str = ',') -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        filename (str): The path to the CSV file.
        delimiter (str): The delimiter used in the CSV file.

    Returns:
        List[Dict[str, str]]: The content of the CSV file as a list
                              of dictionaries.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        return [row for row in reader]


def get_min_price_for_products_in_store(store_prices: Dict[str, str]) -> int:
    """
    Finds the minimum price of any product in a store.

    Args:
        store_prices (Dict[str, str]): Dictionary containing product prices
                                       in a store.

    Returns:
        int: The minimum price of any product in the store.
    """
    return min(
        int(price) for price in store_prices.values() if price.isdigit()
    )


def get_min_prices_for_all_stores(
    data: List[Dict[str, str]]
) -> Dict[str, Dict[str, str]]:
    """
    Finds the minimum price of each product in each store.

    Args:
        data (List[Dict[str, str]]): List of dictionaries containing product
                                     prices in different stores.

    Returns:
        Dict[str, Dict[str, str]]: Dictionary where keys are store names
                                   and values are dictionaries containing
                                   product names and their minimum prices in
                                   each store.
    """
    min_prices_per_store: Dict[str, Dict[str, str]] = {}

    for row in data:
        store: str = row['Магазин']
        min_prices_per_store[store] = {}

        min_price: int = get_min_price_for_products_in_store(row)

        for product, price in row.items():
            if price.isdigit() and int(price) == min_price:
                min_prices_per_store[store][product] = price

    return min_prices_per_store


def get_cheapest_products(
    data_prices: Dict[str, Dict[str, str]]
) -> Dict[str, str]:
    """
    Finds the product with the overall minimum price across all stores.

    Args:
        data_prices (Dict[str, Dict[str, str]]): Dictionary containing product
                                                 prices in different stores.

    Returns:
        Dict[str, str]: Dictionary where keys are store names and values
                        are the product names with the minimum price.
    """
    overall_min_price = min(
        int(price)
        for store_prices in data_prices.values()
        for price in store_prices.values()
        if price.isdigit()
    )

    cheapest_products: Dict[str, str] = {}

    for store, products in data_prices.items():
        for product, price in products.items():
            if int(price) == overall_min_price:
                cheapest_products[store] = product

    return cheapest_products


def get_cheapest_store_and_product(
    products_per_shop: Dict[str, str]
) -> Tuple[str, str]:
    """
    Finds the store and product with the overall minimum price.

    Args:
        products_per_shop (Dict[str, str]): Dictionary containing products and
                                            their prices in different stores.

    Returns:
        Tuple[str, str]: A tuple containing the name of the store and the name
                         of the product with the minimum price.
    """
    min_price_product = min(
        products_per_shop.items(), key=lambda x: (x[1], x[0])
    )
    return min_price_product


def display_result(product: str, store: str) -> None:
    """
    Displays the result in a specified format.

    Args:
        product (str): The name of the product.
        store (str): The name of the store.
    """
    print(f'{product}: {store}')


def display_cheapest_product_and_store(data: List[Dict[str, str]]) -> None:
    """
    Displays the cheapest product and store.

    Args:
        data (List[Dict[str, str]]): List of dictionaries containing product
                                     prices in different stores.
    """
    min_prices = get_min_prices_for_all_stores(data)
    cheapest_products_per_shop = get_cheapest_products(min_prices)
    store, product = get_cheapest_store_and_product(cheapest_products_per_shop)
    display_result(product, store)


data: List[Dict[str, str]] = read_csv(INPUT_FILE, delimiter=';')
display_cheapest_product_and_store(data)

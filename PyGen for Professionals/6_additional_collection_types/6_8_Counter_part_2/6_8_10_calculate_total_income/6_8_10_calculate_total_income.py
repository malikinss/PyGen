'''
TODO:
    To earn extra money, Timur decided to start selling vegetables.

    He has sales data for the year, divided into four files by quarter:
        quarter1.csv, quarter2.csv, quarter3.csv and quarter4.csv.

    In each file, the first column indicates the name of the product, and the
    subsequent columns indicate the amount of the product sold in kilograms
    for a certain month:
        product,January,February,March
        Potatoes,39,61,3
        Daikon,51,96,83
        ...

    There is also a prices.json file containing a dictionary in which the key
    is the name of the product, and the value is the price per kilogram
    in rubles:
        {
        "Potatoes": 53,
        "Daikon": 55,
        ...
        }

    Write a program that outputs a single number - the amount Timur earned for
    the year selling vegetables.
'''
import csv
import json
from collections import Counter
from typing import List, Dict


def read_csv_file(filename: str,
                  delimiter: str = ',') -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        filename: The path to the CSV file.
        delimiter: The delimiter used in the CSV file.

    Returns:
        The content of the CSV file as a list of dictionaries.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        return [row for row in reader]


def read_json_file(file_path: str) -> List[Dict[str, str]]:
    """
    Read JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict[str, str]]: List of dictionaries containing JSON data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def parse_monthly_purchases(record: Dict[str, str]) -> Counter:
    """
    Parse monthly purchases from a record.

    Args:
        record: Dictionary with product sales data for one month.

    Returns:
        Counter object with product names and amounts sold.
    """
    monthly_purchases = Counter()
    product_name = record['продукт']

    for month, value in record.items():
        if month == 'продукт':
            continue
        monthly_purchases[product_name] += int(value)

    return monthly_purchases


def count_quarterly_purchases(quarter_number: int) -> Counter:
    """
    Count the purchases for a specific quarter.

    Args:
        quarter_number: The quarter number (1 to 4).

    Returns:
        Counter object with total product amounts for the quarter.
    """
    quarterly_purchases = Counter()
    current_quarter_path = f'{folder}quarter{quarter_number}.csv'
    quarter_data = read_csv_file(current_quarter_path)

    for record in quarter_data:
        monthly_purchases = parse_monthly_purchases(record)
        quarterly_purchases.update(monthly_purchases)

    return quarterly_purchases


def count_total_purchases() -> Counter:
    """
    Count the total purchases from all quarters.

    Returns:
        A Counter object with the total amount of each product sold.
    """
    total_purchases = Counter()

    for i in range(1, 5):
        quarterly_purchases = count_quarterly_purchases(i)
        total_purchases.update(quarterly_purchases)

    return total_purchases


def calculate_total_income(purchases: Counter,
                           prices: Dict[str, int]) -> Counter:
    """
    Calculate the total income from all products.

    Args:
        purchases: Counter object with total product amounts.
        prices: Dictionary with product prices.

    Returns:
        Counter object with total income for each product.
    """
    total_income = Counter()

    for product, amount in purchases.items():
        product_price = prices[product]
        total_income[product] = amount * product_price

    return total_income


if __name__ == '__main__':
    folder = '6_8_10/tests/'
    prices_path = f'{folder}prices.json'
    prices = read_json_file(prices_path)

    total_purchases = count_total_purchases()
    total_income = calculate_total_income(total_purchases, prices)

    # Print the total income earned for the year
    print(total_income.total())

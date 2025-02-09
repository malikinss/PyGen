'''
TODO:
    A text file is available to you ledger.txt with the company's sales data
    for the month.

    Each line of the file shows how much the customer paid for the product,
    in dollars (an integer).

    Write a program to calculate the total monthly revenue of the company.

NOTE:
    Assume that the executable program and the specified file are in the same
    folder.
'''


def read_data_from_file(file_name: str):
    """
    Reads the content of a file and returns a list of lines.

    Args:
        file_name (str): The name of the file.

    Returns:
        list: A list of lines from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as given_file:
        return given_file.readlines()


def get_payments_from_data(data: list) -> list:
    """
    Converts a list of payment data (strings) into a list of integers.

    Args:
        data (list): A list of strings, each representing a payment.

    Returns:
        list: A list of integers representing the payment amounts.
    """
    return [int(line.lstrip('$')) for line in data]


def calculate_total_revenue(file_name: str) -> int:
    """
    Reads the sales data from a file and calculates the total revenue.

    Args:
        file_name (str): The name of the sales data file.

    Returns:
        int: The total revenue from the sales data.
    """
    sales_data = read_data_from_file(file_name)
    payments = get_payments_from_data(sales_data)
    return sum(payments)


# Calculate total revenue and print it
total_revenue = calculate_total_revenue('ledger.txt')
print(f"${total_revenue}")

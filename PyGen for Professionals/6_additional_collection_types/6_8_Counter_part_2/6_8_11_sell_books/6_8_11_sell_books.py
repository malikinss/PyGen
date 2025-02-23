'''
TODO:
    Timur sells math books for grades 1-11.

    He has a list of all the books he has in stock.

    n customers come to Timur, state the class number they want to buy a book
    for and the amount they are willing to pay, and if the book is in stock,
    Timur sells it.

    Write a program that calculates the total amount of money Timur will earn
    selling books.

    The first line of the program is fed with a sequence of numbers separated
    by a space, representing a set of books that are in stock.

    Each number in the sequence is a book for the specified class, for example,
    the sequence 1 1 4 represents a set of two books for the first grade and
    one book for the fourth grade.

    The second line contains the number n — the number of customers.

    The next n lines contain two numbers separated by a space, where:
        the first number is the class number;
        the second is the amount offered by the customer.

    The program should output a single number:
        the total amount of money Timur earned.

NOTE:
    Let's look at the first test.

    The first line contains a list of books that are available:
        2 books for 1st grade
        1 book for 11th grade
        3 books for 9th grade
        2 books for 5th grade
        1 book for 7th grade

    The next line contains the number 7 — the number of buyers. The next 7
    lines contain the class number and some amount:
        the first buyer buys a book for the 1st class for 300 rubles
        the second buyer buys a book for the 1st class for 250 rubles
        the third buyer buys a book for the 11th class for 400 rubles

    there are no more books for the 1st class in stock, so the purchase is
    impossible

        the fifth buyer buys a book for the 7th class for 200 rubles
        the sixth buyer buys a book for the 9th class for 400 rubles

    there are no more books for the 7th class in stock, so the purchase is
    impossible

    In total, Timur earned
        300 + 250 + 400 + 200 + 400 = 1550 rubles.
'''
from collections import Counter


def sell_book(
    available_books: Counter, class_number: int, given_price: int
) -> int:
    """
    Simulates the selling process for each customer.

    Args:
        available_books: Counter object with available books per class.
        class_number: The class number the customer wants to buy.
        given_price: The amount the customer is willing to pay.

    Returns:
        int: The amount earned from selling the book, or 0 if the book is
        not available.
    """
    if available_books[class_number] > 0:
        available_books[class_number] -= 1
        return given_price
    return 0


def sell_books(available_books: Counter, customers: list) -> int:
    """
    Sells books to customers based on available stock and customer requests.

    Args:
        available_books: Counter object representing available books per class.
        customers: List of tuples (class_number, price).

    Returns:
        int: Total income earned from selling books.
    """
    total_income = 0

    for class_number, price in customers:
        total_income += sell_book(available_books, class_number, price)

    return total_income


if __name__ == '__main__':
    # Reading available books (class_number counts)
    available_books = Counter(map(int, input().split()))

    # Reading the number of customers
    n = int(input())

    # Reading customer requests (class_number and price offered)
    customers = [tuple(map(int, input().split())) for _ in range(n)]

    # Calculate the total income
    total_income = sell_books(available_books, customers)

    # Output the total income
    print(total_income)

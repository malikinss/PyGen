'''
TODO:
    Students in the 10th grade of the online school BEEGEEK were given the
    task of reading three books during the summer holidays:
        - "What is Mathematics?";
        - "The Mathematical Component";
        - "100 Brilliant Ideas in Mathematics".

    It turned out that n students read the first book, m students read
    the second, k students read the third.

    It is also known that x students read the first or second, or both
    of these books, y students read the second or third, or both, z students
    read the first and third, or at least one of these two books.

    Only t students completed the task.

    There are a students in the 10th grade.

    Write a program that displays how many students:
        - read only one book
        - read only two books
        - did not read any of the recommended books
'''
from typing import Tuple


def book_reading_stats(
    n: int, m: int, k: int, x: int, y: int, z: int, t: int, a: int
) -> Tuple:
    """
    Calculate statistics on how many students read only one book,
    only two books, and how many did not read any of the recommended books.

    Args:
    n (int): Number of students who read the first book.
    m (int): Number of students who read the second book.
    k (int): Number of students who read the third book.
    x (int): Number of students who read the first or second book, or both.
    y (int): Number of students who read the second or third book, or both.
    z (int): Number of students who read the first and third book,
             or at least one of these two books.
    t (int): Number of students who completed the task
             (read at least one book).
    a (int): Total number of students in the grade.

    Returns:
    Tuple: A tuple containing:
        - The number of students who read only one book.
        - The number of students who read only two books.
        - The number of students who did not read any book.
    """
    # Calculate students who read only one book
    only_1_and_2 = n + m - x - t
    only_2_and_3 = m + k - y - t
    only_1_and_3 = k + n - z - t

    # Only one book
    only_1 = (n - only_1_and_2 - only_1_and_3 - t)
    only_2 = (m - only_1_and_2 - only_2_and_3 - t)
    only_3 = (k - only_2_and_3 - only_1_and_3 - t)

    only_one = only_1 + only_2 + only_3

    # Only two books
    only_two = only_1_and_2 + only_2_and_3 + only_1_and_3

    # Students who did not read any books
    did_not_read = a - only_one - only_two - t

    return (only_one, only_two, did_not_read)


# Input values
n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]

# Calculate and print the results
only_one, only_two, did_not_read = book_reading_stats(n, m, k, x, y, z, t, a)

print(only_one)  # Number of students who read only one book
print(only_two)  # Number of students who read only two books
print(did_not_read)  # Number of students who did not read any book

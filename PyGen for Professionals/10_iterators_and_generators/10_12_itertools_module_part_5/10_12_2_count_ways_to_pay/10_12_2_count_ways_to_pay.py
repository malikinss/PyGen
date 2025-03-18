'''
TODO:
    Timur came to the bookstore to buy a new book on mathematics, the cost of
    which is $100.

    He has a lot of bills of different denominations in his wallet,
    which are presented in the wallet list.

    For example, Timur can pay with one $100 bill or two $50 bills.

    Complete the code below so that it displays the number of ways Timur can
    buy a book worth $100.

NOTE:
    The ways to pay with sets of bills of the type 50, 20, 20, 10
    and 20, 10, 50, 20 are considered the same and should not be counted twice.
'''
from itertools import combinations


def count_ways_to_pay(wallet, target_amount):
    """
    Counts the number of unique ways to pay a specific target amount using
    bills from the wallet.

    Args:
        wallet (list[int]): List of available bills of different denominations.
        target_amount (int): The target amount to pay (in this case, 100).

    Returns:
        int: The number of unique ways to pay the target amount.
    """
    combs = set()

    for i in range(1, len(wallet) + 1):
        for comb in combinations(wallet, r=i):
            if sum(comb) == target_amount:
                combs.add(tuple(sorted(comb)))

    return len(combs)


wallet = [
    100, 100,
    50, 50, 50, 50,
    20, 20, 20,
    10, 10, 10, 10, 10,
    5, 5,
    1, 1, 1, 1, 1
]
target_amount = 100

print(count_ways_to_pay(wallet, target_amount))

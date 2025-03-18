'''
TODO:
    Timur came to the bookstore to buy a new book on mathematics, the cost of
    which is $100.

    He has an unlimited number of bills in his wallet, the denominations of
    which are presented in the wallet list.

    In other words, Timur can use a bill of one denomination any number of
    times.

    For example, he can pay with five $20 bills or ten $10 bills.

    Complete the code below so that it displays the number of ways Timur can
    buy a book worth $100.

NOTE:
    The ways to pay with sets of bills of the type 50, 20, 20, 10
    and 20, 10, 50, 20 are considered the same and should not be counted twice.
'''
from itertools import combinations_with_replacement


def count_ways_to_pay(wallet, target_amount):
    """
    Counts the number of unique ways to pay a specific target amount using
    bills from the wallet, where each bill can be used an unlimited number
    of times.

    Args:
        wallet (list[int]): List of available bills of different denominations.
        target_amount (int): The target amount to pay (in this case, 100).

    Returns:
        int: The number of unique ways to pay the target amount.
    """
    combs = set()

    for i in range(1, target_amount // min(wallet) + 1):
        for comb in combinations_with_replacement(wallet, r=i):
            if sum(comb) == target_amount:
                combs.add(tuple(sorted(comb)))

    return len(combs)


wallet = [100, 50, 20, 10, 5]
target_amount = 100

print(count_ways_to_pay(wallet, target_amount))

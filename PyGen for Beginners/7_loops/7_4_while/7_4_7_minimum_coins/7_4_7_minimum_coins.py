'''
TODO:
    Everyone knows that the witcher is able to defeat any monsters,
    but his services will cost a lot.

    In addition, the witcher does not accept banknotes,
    he only accepts minted coins.

    In the world of the witcher, there are coins with denominations
    of 1, 5, 10, 25.

    Write a program that determines the minimum number of minted coins
    to be paid to the witcher.
'''


def minimum_coins(n: int) -> int:
    """
    Determines the minimum number of minted coins needed to reach
    a given amount.

    In the witcher's world, coins are available in denominations
    of 1, 5, 10, and 25.

    Args:
        n (int): The total amount to be paid in coins.

    Returns:
        int: The minimum number of coins required to make the given amount.
    """
    denominations = [25, 10, 5, 1]
    counter = 0

    for coin in denominations:
        while n >= coin:  # While n is greater than or equal to the coin value
            counter += 1  # Use one coin of this denomination
            n -= coin  # Subtract the coin value from n

    return counter


# Input
n = int(input("Enter the amount to be paid: "))

# Output the result
print("Minimum coins required:", minimum_coins(n))

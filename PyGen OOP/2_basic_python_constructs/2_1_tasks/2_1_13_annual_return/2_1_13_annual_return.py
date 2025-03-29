'''
TODO:
    Almost everyone is familiar with financial investments, the purpose of
    which is to increase available funds over a period of time.

    The simplest example is a bank deposit, which increases annually by
    accruing a certain amount of interest on it.

    The components of such a bank deposit are the initial deposit amount,
    the interest rate, and the deposit term.

    To understand how the deposit amount changes and how interest is accrued,
    consider the following problem:
        A depositor opened an account in a bank, placing an amount of 120,000
        rubles at 10% per annum.

        What amount will be in the account after 3 years?

        Solution:
            At the end of each year, the deposit amount increases by 10%.

        According to the problem statement, we have:
            Deposit amount after the 1st accrual:
                120000 * (11 / 10) = 132000
            Deposit amount after the 2nd accrual:
                132000 * (11 / 10) = 145200
            Deposit amount after the 3rd accrual:
                145200 * (11 / 10) = 159720

        Answer:
            159720 rubles.

    Implement the generator function annual_return(), which accepts three
    arguments in the following order:
        - start — an integer, the initial deposit amount in rubles
        - percent — an integer, the percentage by which the current deposit
                    amount will increase each year
        - years — an integer, the number of years during which interest will
                  be accrued

    The function must return an iterator simulating a bank deposit.

    The returned values of the iterator must be the deposit amounts after the
    next percent accrual.
'''


def annual_return(start: int, percent: int, years: int) -> iter:
    """
    A generator function that simulates a bank deposit with interest accrual
    over time.

    Each year, the deposit amount is increased by a given percentage.

    Args:
        start (int): The initial deposit amount in rubles.
        percent (int): The annual interest rate (percentage).
        years (int): The number of years the deposit will accrue interest.

    Yields:
        float: The deposit amount after the annual interest accrual for each
        year.
    """
    for _ in range(years):
        start += start * (percent / 100)
        yield round(start, 2)

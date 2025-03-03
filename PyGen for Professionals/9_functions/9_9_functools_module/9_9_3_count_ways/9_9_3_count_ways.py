'''
TODO:
    Dima likes to study, but he doesn't like getting low grades, and he's most
    upset by bad grades.

    That's why when Dima gets to his apartment by stairs, he climbs only one,
    three, or four steps, but not two.

    Implement the ways() function that takes one argument:
        n is a natural number (n≤ 100)

    The function should return a single number — the number of ways to climb
    the n-th step.

    The path starts from the first step, and you can climb only one, three, or
    four steps.

NOTE:
    Let's look at the first test.
    You can climb the fifth step in the following four ways:
        1→2→3→4→5
        1→4→5
        1→2→5
        1→5
'''
from functools import lru_cache


def count_ways(n: int) -> int:
    """
    Calculate the number of ways to climb to the n-th step.

    Args:
        n (int): The step number to reach.

    Returns:
        result (int): The number of ways to reach the n-th step.
    """

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    @lru_cache
    def count_inner_ways(n: int) -> int:
        """
        Helper function that recursively calculates the number of ways
        to reach the n-th step.

        Args:
            n (int): The step number to reach.

        Returns:
            result (int): The number of ways to reach the n-th step.
        """
        if n < 4:
            return 1
        elif n == 4:
            return 2
        else:
            return count_inner_ways(n-1) + count_inner_ways(n-3) + count_inner_ways(n-4)

    return count_inner_ways(n)

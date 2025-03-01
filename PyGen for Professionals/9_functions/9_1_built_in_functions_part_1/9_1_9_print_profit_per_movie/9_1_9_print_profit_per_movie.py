"""
TODO:
    There are three lists available: names, budgets, and box_offices.

    The first list contains the names of different movies, the second and
    third lists contain their budgets and box office receipts in dollars.

    Complete the code below so that it determines how much profit each movie
    made and prints the names of the movies, along with their profits.

    The movies should be listed lexicographically, each on a separate line, in
    the following format:
        <movie>: <profit>$

NOTE:
    Profit is defined as the box office receipt minus the budget.

    The initial part of the answer looks like this:
        Cars: 342216280$
        Coco: 627082196$
        Finding Nemo: 846335536$
        ...

    The zip() function is useful in the problem.
"""
from typing import List


def print_profit_per_movie(
    names: List[str],
    budgets: List[int],
    box_offices: List[int]
) -> None:
    """
    Calculates and prints the profit for each movie.

    Args:
        names (List[str]): List of movie names.
        budgets (List[int]): List of movie budgets.
        box_offices (List[int]): List of movie box office receipts.

    Returns:
        None
    """
    if not (len(names) == len(budgets) == len(box_offices)):
        raise ValueError("All input lists must have the same length.")

    # Calculate profits by subtracting the budget from the box office receipt
    movie_profits = [
        (name, box_office - budget)
        for name, budget, box_office in zip(names, budgets, box_offices)
    ]

    # Sort the movie profits list by movie name lexicographically
    for movie, profit in sorted(movie_profits):
        print(f'{movie}: {profit}$')


# Example lists of movie data
names = [
    'Moana', 'Cars', 'Zootopia', 'Ratatouille',
    'Coco', 'Inside Out', 'Finding Nemo', 'Frozen'
]
budgets = [
    150000000, 120000000, 150000000, 150000000,
    180000000, 175000000, 94000000, 150000000
]
box_offices = [
    643331111, 462216280, 1023784195, 620702951,
    807082196, 857611174, 940335536, 1280802282
]

# Call the function to print the profits
print_profit_per_movie(names, budgets, box_offices)

'''
TODO:
    In the first year, there are 77 frogs in the pond.

    Each year, 30 frogs are caught from the pond, and the remaining ones
    reproduce, and their number increases threefold.

    So, the number of frogs in the k-th year can be described by the formula:
        Fk = 3(F(k-1) - 30)

    Implement the function number_of_frogs() using recursion, which takes
    one argument:
        - year is a natural number

    The function should return a single number — the number of frogs in the
    pond in the year.
'''


def number_of_frogs(year: int) -> int:
    """
    Calculate the number of frogs in the pond in a given year.

    Args:
        year (int): The year for which the number of frogs is calculated.

    Returns:
        int: The number of frogs in the pond in the given year.
    """
    def calculate_frogs(year: int, value: int = 77) -> int:
        """
        Recursively calculate the number of frogs for a specific year.

        Args:
            year (int): The year for which the number of frogs is calculated.
            value (int): The current number of frogs.

        Returns:
            int: The number of frogs in the pond in the given year.
        """
        if year == 1:
            return value

        return calculate_frogs(year - 1, (value - 30) * 3)

    return calculate_frogs(year)


print(number_of_frogs(int(input())))

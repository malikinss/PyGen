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
    Calculate the number of frogs in the pond in the given year using
    recursion.

    Args:
        year (int): The year for which the number of frogs is to be calculated.

    Returns:
        int: The number of frogs in the pond in the given year.
    """
    def calculate_frogs(current_year: int, frogs: int) -> int:
        """
        Recursively calculates the number of frogs for a specific year.

        Args:
            current_year (int): The current year for the calculation.
            frogs (int): The current number of frogs.

        Returns:
            int: The number of frogs in the pond in the given year.
        """
        # Base case: year 1 starts with 77 frogs
        if current_year == 1:
            return frogs

        # Recursive case: each year, the frogs are multiplied by 3
        # after catching 30
        return calculate_frogs(current_year - 1, (frogs - 30) * 3)

    # Start the recursive calculation from year 1 with an initial frog
    # count of 77
    return calculate_frogs(year, 77)


# Test the function with an input year
print(number_of_frogs(int(input())))

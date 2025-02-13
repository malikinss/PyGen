'''
TODO:
    From 1950 to 2017, Florida was hit by a total of 235 hurricanes.

    The florida_hurricane_dates variable stores a list of dates on which
    a hurricane occurred.

    The Atlantic hurricane season officially begins on June 1st.

    Complete the code below to print the number of hurricanes since 1950 that
    hit Florida before the official start of hurricane season.

NOTE:
    Assume that the florida_hurricane_dates variable is declared and available
    to your program.

    Assume that the date type is already imported into the program.

'''


def count_early_hurricanes(hurricane_dates: list) -> int:
    """
    Count the number of hurricanes that hit Florida before the official start
    of the Atlantic hurricane season.

    Args:
    - hurricane_dates (list): A list of date objects representing the dates
                              of hurricanes.

    Returns:
    - int: The number of hurricanes that occurred before June 1st.
    """
    early_hurricanes = 0
    for hurricane in hurricane_dates:
        # Check if the hurricane occurred before June (month < 6)
        if hurricane.month < 6:
            early_hurricanes += 1

    return early_hurricanes

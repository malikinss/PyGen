'''
TODO:
    The number 13 has long been considered diabolical.

    This has its own explanation, and more than one: there are interpretations
    related to the Last Supper - where Christ and the 12 apostles were, one of
    whom became a traitor.

    There is a belief that a Sabbath requires 12 witches and Satan.

    In history, the number 13 in conjunction with Friday became “unlucky” in
    1307, when King Philip the Fair of France gave the order to capture
    all the Templars - members of the knightly order of the crusaders.

    All of them were burned at the stake of the Inquisition, and this happened
    on Friday, April 13.

    Prove that the 13th of the month most often falls on a Friday.

    Write a program that calculates how many thirteenth numbers there are for
    each day of the week in the period from 01/01/0001 to 31/12/9999.
'''

from datetime import datetime
from collections import Counter
from typing import Dict


def count_thirteenth_days(start_year: int, end_year: int) -> Dict[str, int]:
    """
    Counts occurrences of the 13th day of the month for each day of the week.

    Args:
        start_year (int): Starting year of the range.
        end_year (int): Ending year of the range.

    Returns:
        Dict[str, int]: A dictionary mapping each weekday to its count.
    """
    weekday_count: Dict = Counter()

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            thirteenth = datetime(year, month, 13)
            weekday_name = thirteenth.strftime('%A')
            weekday_count[weekday_name] += 1

    return weekday_count


def display_weekday_counts(weekday_counts: Dict[str, int]) -> None:
    """
    Displays counts of the 13th for each weekday.

    Args:
        weekday_counts (Dict[str, int]): Dictionary with weekday names as keys
                                         and counts as values.
    """
    for count in weekday_counts.values():
        print(count)


# Compute and display the results
weekday_counts = count_thirteenth_days(1, 9999)
display_weekday_counts(weekday_counts)

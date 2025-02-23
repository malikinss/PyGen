'''
TODO:
    Implement a print_bar_chart() function that takes two arguments in the
    following order:
        - data is a string or list of strings
        - mark is a single character

    The function should determine:
        - how many times each character appears in the string, if data is
        a string
        - how many times each string appears in the list, if data is a list

    Then the function should print the result as a bar chart, indicating each
    character (string) and its count.

    The count is displayed as the mark character repeated the appropriate
    number of times, for example, if mark='+', a count of four would be
    displayed as ++++.

    The characters (strings) in the chart should be ordered by decreasing
    count, or in their original order if the count is equal, each on a
    separate line, in the following format:
        <character or string> |<count>

NOTE:
    Note the second test, the function should add the required number of
    spaces if the string is shorter than the others.

    The program must be case-sensitive.
    That's, for example, the strings Python and python are considered
    different.
'''
from collections import Counter
from typing import Union, List, Tuple


def get_sorted_counts(data: Union[str, List[str]]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples with elements and their counts, sorted by
    their frequency in descending order.

    Args:
        data (Union[str, List[str]]): The input data, either a string or
        a list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples with elements and their counts,
        sorted by frequency in descending order.
    """
    return Counter(data).most_common()


def print_bar_chart(data: Union[str, List[str]], mark: str) -> None:
    """
    Prints a bar chart representing the frequency of elements in the data.

    Args:
        data (Union[str, List[str]]): The input data, which can be a string or
        a list of strings.
        mark (str): A single character used to create the bar chart.
    """
    # Get the sorted counts of characters or strings
    sorted_counts = get_sorted_counts(data)

    # Determine the maximum length of item names for consistent formatting
    max_item_length = max(len(item) for item, _ in sorted_counts)

    # Print each element and its count represented by the mark character
    for item, count in sorted_counts:
        # Use ljust to pad the item name to align with the longest item
        print(f'{item.ljust(max_item_length)} |{mark * count}')


# Example usage
if __name__ == '__main__':
    print_bar_chart('beegeek', '+')
    print_bar_chart(['apple', 'banana', 'apple', 'cherry'], '*')

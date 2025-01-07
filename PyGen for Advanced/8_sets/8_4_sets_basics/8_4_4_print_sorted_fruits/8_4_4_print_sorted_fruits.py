'''
TODO:
    Complete the code below so that it prints the elements of the fruits set,
    each on a separate line, sorted in descending order (in reverse
    lexicographic order).
'''
from typing import Set


def print_sorted_fruits(fruits: Set[str]) -> None:
    """
    Prints the elements of the given set of fruits, each on a separate line,
    sorted in descending (reverse lexicographic) order.

    Args:
    fruits (Set[str]): A set of fruit names (strings).
    """
    reversed_fruits = sorted(fruits, reverse=True)
    print(*reversed_fruits, sep="\n")


fruits = {
    'apple', 'banana', 'cherry', 'avocado',
    'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'
}
print_sorted_fruits(fruits)

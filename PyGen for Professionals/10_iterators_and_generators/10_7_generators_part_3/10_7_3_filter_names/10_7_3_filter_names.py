'''
TODO:
    Implement a generator function filter_names() that takes three arguments
    in the following order:
        names — a list of names
        ignore_char — a single character
        max_names — a natural number

    The function should return a generator that produces max_names names from
    the names list, ignoring names that begin with ignore_char (in any case)
    contain at least one digit

    If max_names is greater than the number of names in the names list, then
    the generator should produce all possible names from this list.

NOTE
    The names in the generator returned by the function must be in their
    original order.
'''
from typing import Iterator, Iterable


def filter_names(
    names: Iterable[str], ignore_char: str, max_names: int
) -> Iterator[str]:
    """
    Filters names based on given conditions and returns a generator.

    Args:
        names (Iterable[str]): A list or iterable of names.
        ignore_char (str): A single character (case insensitive).
                           Names starting with this character are ignored.
        max_names (int): The maximum number of names to yield.

    Returns:
        Iterator[str]: A generator yielding up to max_names names,
                       skipping names that start with ignore_char or contain
                       digits.
    """

    def is_valid_name(name: str) -> bool:
        """
        Checks if a name is valid.
        """
        has_digits = any(char.isdigit() for char in name)
        starts_with_ignore_char = name.lower().startswith(ignore_char.lower())
        return not has_digits and not starts_with_ignore_char

    # Using generator expression to filter names
    filtered_names = (name for name in names if is_valid_name(name))

    # Limiting the output to max_names
    return (name for _, name in zip(range(max_names), filtered_names))

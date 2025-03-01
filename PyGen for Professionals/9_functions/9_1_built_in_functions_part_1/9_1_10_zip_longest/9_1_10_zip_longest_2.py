'''
TODO:
        As you already know, the zip() function concatenates elements of
        different sequences.

        A special feature of the function is that when passing sequences of
        different lengths, elements of the longer sequence will be discarded.

        Implement the zip_longest() function, which takes a variable number of
        positional arguments, each of which is a list, and one optional named
        argument fill, which has a default value of None.

        The function should concatenate elements of the passed sequences into
        tuples, similar to the zip() function, and return them as a list, but
        if the sequences have different lengths, the missing elements of the
        shorter sequences should take the fill value.

NOTE:
        Consider the first test with the following call:
            zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_')

        The first list has a length of 5, the second - 3, that is, elements 4
        and 5 from the first list have no pairs from the second list.

        In this case, the function should match them with a fill value of '_'.

        So, the result of the function will be a list:
            [(1, 'a'), (2, 'b'), (3, 'c'), (4, '_'), (5, '_')]
'''
from typing import Iterable, Any


def find_max_length(*lists: Iterable) -> int:
    """
    Find the maximum length among the given iterables.

    Args:
        *lists (Iterable): A variable number of iterable objects.

    Returns:
        max_length (int): The maximum length found among the iterables.
    """
    if not lists:
        return 0
    return max(len(lst) for lst in lists)


def create_fillers(iterable: Iterable, max_len: int, fill: Any) -> list:
    """
    Create a list of filler elements to match the required length.

    Args:
        iterable (Iterable): The current iterable to be extended.
        max_len (int): The target length to match.
        fill (Any): The filler value for missing elements.

    Returns:
        fillers (list): A list of filler elements.
    """
    return [fill] * (max_len - len(iterable))


def extend_with_fill(iterable: Iterable, max_len: int, fill: Any) -> list:
    """
    Extend the given iterable with filler elements if it is shorter
    than max_len.

    Args:
        iterable (Iterable): The current iterable to be extended.
        max_len (int): The target length to match.
        fill (Any): The filler value for missing elements.

    Returns:
        extended_list (list): The extended list with filler elements added.
    """
    fillers = create_fillers(iterable, max_len, fill)

    return list(iterable) + fillers


def zip_longest(*args: Iterable, fill: Any = None) -> list[tuple]:
    """
    Zip elements from multiple iterables, filling missing values with a
    specified value.

    Args:
        *args (Iterable): A variable number of iterable objects to be zipped.
        fill (Any, optional): The value to fill in for missing elements.
        Defaults to None.

    Returns:
        zipped_list (list[tuple]): A list of tuples containing zipped elements.

    Raises:
        ValueError: If no iterables are provided or if non-iterable arguments
        are passed.
    """
    if not args:
        raise ValueError("At least one iterable argument is required.")

    try:
        max_len = find_max_length(*args)
    except TypeError:
        raise ValueError("All arguments must be iterable.")

    new_args = []

    for iterable in args:
        if len(iterable) < max_len:
            extended_iterable = extend_with_fill(iterable, max_len, fill)
            new_args.append(extended_iterable)
        else:
            new_args.append(iterable)

    return list(zip(*new_args))


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))

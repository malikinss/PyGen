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


def is_index_out_of_range(id: int, obj: Iterable) -> bool:
    """
    Check if the index is out of range for the given iterable.

    Args:
        id (int): The index to check.
        obj (Iterable): The iterable object.

    Returns:
        bool: True if the index is out of range, otherwise False.
    """
    return id > (len(obj) - 1)


def zip_longest(*args: Iterable, fill: Any = None) -> list[tuple]:
    """
    Combine elements of multiple iterables into tuples. If iterables have
    different lengths, fill missing values with the specified fill value.

    Args:
        *args (Iterable): Variable number of iterable objects.
        fill (Any, optional): The value to use for missing elements. Defaults
        to None.

    Returns:
        list[tuple]: A list of tuples containing combined elements.
    """
    try:
        max_len = find_max_length(*args)
    except TypeError:
        raise ValueError("All arguments must be iterable.")

    zipped = []

    for i in range(max_len):
        current_tuple_elements = []

        for current_iterable in args:
            if is_index_out_of_range(i, current_iterable):
                current_element = fill
            else:
                current_element = current_iterable[i]

            current_tuple_elements.append(current_element)

        zipped.append(tuple(current_tuple_elements))

    return zipped


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))

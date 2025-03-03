'''
TODO:
    As you know, the map() function takes a function and an iterable object
    and returns an iterator whose elements are the elements of the iterable
    object to which the passed function was applied.

    Often, the elements of the iterable object are collections
    (lists, tuples, ..), then inside the passed function we have to access
    each element of these collections by index.

    For example:
        persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]
        full_names = map(lambda tup: tup[0] + ' ' + tup[1], persons)

    It would be convenient to have a function, let's call it starmap(), that
    would accept a function with not one argument, but several — each element
    of the collection:
        persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]
        full_names = starmap(lambda name,
                                    surname: f'{name} {surname}',
                             persons)

    Implement the starmap() function using the map() function, which takes
    two arguments:
        func — a function
        iterable — an iterable whose elements are collections

    The starmap() function should work similarly to the map() function, that
    is, return an iterator whose elements are elements iterable
    object iterable, to which the function func was applied,
    with the only difference:
        func must take not one argument - a collection (an element of iterable)
        but each element of this collection as an independent argument.
'''
from typing import List, Callable, Iterable, Any


def transpose_collections(collections: List[List[Any]]) -> List[List[Any]]:
    """
    Transpose a list of collections.

    Args:
        collections (List[List[Any]]): A list where each element is
        a collection.

    Returns:
        List[List[Any]]: The transposed list of collections.
    """
    return [list(row) for row in zip(*collections)]


def starmap(function: Callable[..., Any],
            collections: Iterable[Iterable[Any]]) -> Iterable[Any]:
    """
    Apply a function to unpacked elements of each collection in an iterable.

    Args:
        function (Callable[..., Any]): A function that takes multiple
        arguments.
        collections (Iterable[Iterable[Any]]): An iterable where each element
        is a collection.

    Returns:
        Iterable[Any]: An iterator yielding the results of applying the
        function to the unpacked elements.
    """
    return map(function, *transpose_collections(collections))

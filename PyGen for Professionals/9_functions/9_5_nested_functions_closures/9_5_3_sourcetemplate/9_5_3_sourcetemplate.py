'''
TODO:
        Query string — the part of the URL containing keys and their values.

        It starts after the question mark and goes to the end of the address.

        For example:
            https://beegeek.ru?name=timur # query string: name=timur

        If there are several parameters in the query string, they are
        separated by the ampersand &:
            https://beegeek.ru?name=timur&color=green # query string:
            name=timur&color=green

        Implement the sourcetemplate() function that takes one argument:
        url — URL address

        The sourcetemplate() function must return a function that takes
        an arbitrary number of named arguments and returns the URL address
        concatenated with the query string formed from the passed arguments.

        When called without arguments, it must return the original URL address
        without changes.
NOTE:
        Parameters in the query string must be arranged in lexicographic order
        of keys.
'''
from typing import Callable, Dict


def sourcetemplate(url: str) -> Callable:
    """
    Returns a function that generates a URL with query parameters.

    Args:
        url (str): Base URL.

    Returns:
        inner (Callable): Function that returns the URL with query parameters.
    """
    def generate_query_string(params: Dict[str, str]) -> str:
        """
        Generates a query string from the provided parameters.

        Args:
            params (Dict[str, str]): Dictionary of query parameters.

        Returns:
            query_string (str): Formatted query string.
        """
        sorted_keys = sorted(params.keys())
        query_string_lst = [f'{key}={params[key]}' for key in sorted_keys]

        return '&'.join(query_string_lst)

    def inner(**kwargs: Dict[str, str]) -> str:
        """
        Returns the URL with the query string based on the provided arguments.

        Args:
            kwargs (Dict[str, str]): Named arguments representing query
            parameters.

        Returns:
            url (str): URL with the query string or the original URL.
        """
        nonlocal url

        if kwargs:
            query_string = generate_query_string(kwargs)
            url += f'?{query_string}'

        return url

    return inner

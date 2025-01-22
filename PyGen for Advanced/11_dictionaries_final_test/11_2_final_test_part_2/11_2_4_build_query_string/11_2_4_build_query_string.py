'''
TODO:
    Query string is a part of the URL containing keys and their values.

    It starts after the question mark and goes to the end of the address.

    For example:
        https://beegeek.ru?name=timur # query string: name=timur

    If there are several parameters in the query string, they are separated by
    the ampersand symbol &:
        # query string: name=timur&color=green
        https://beegeek.ru?name=timur&color=green

    Write a function build_query_string() that takes a dictionary with
    parameters as input and returns a query string formed from these
    parameters.

NOTE:
    In the final string, the parameters must be sorted in lexicographic order
    of the dictionary keys.

    You do not need to call the build_query_string() function, you only need
    to implement it.
'''


def build_query_string(params: dict) -> str:
    """
    Builds a query string from the given dictionary of parameters.

    Args:
        params (dict): A dictionary where keys and values represent query
                       parameters and their respective values.

    Returns:
        str: A query string with parameters sorted in lexicographic order.
    """
    # Sort parameters by key and construct key=value pairs
    parameters_list = [
        f"{key}={value}" for key, value in sorted(params.items())
    ]

    # Join all pairs with '&' to form the final query string
    return '&'.join(parameters_list)

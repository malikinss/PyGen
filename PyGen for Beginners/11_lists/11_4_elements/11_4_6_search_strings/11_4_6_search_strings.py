'''
TODO:
    The input to the program is a natural number n, then n lines,
    then the number k — the number of search requests, then k lines —
    search requests.

    Write a program that prints out all the input strings that contain
    all search queries at the same time.
'''


def search_strings(strings: list[str], search_queries: list[str]) -> list[str]:
    """
    Returns a list of strings that contain all search queries,
    case insensitive.

    Args:
        strings (list[str]): List of input strings.
        search_queries (list[str]): List of search queries.

    Returns:
        list[str]: List of strings that match all search queries.
    """
    search_queries = [query.lower() for query in search_queries]
    return [
        s for s in strings
        if all(query in s.lower() for query in search_queries)
    ]


# Input reading
strings = [input() for _ in range(int(input()))]

# List of search queries
search_queries = [input() for _ in range(int(input()))]

# Search and output the result
result = search_strings(strings, search_queries)
print("\n".join(result))

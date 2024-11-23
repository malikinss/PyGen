'''
TODO:
    The input to the program is a natural number n, then n lines,
    then one more line — the search query.

    Write a program that prints out all the input lines that match
    the search term.
'''


def search_lines(n: int, lines: list[str], search_term: str) -> list[str]:
    """
    Finds and returns all lines that match the search term (case-insensitive).

    Args:
        n (int): The number of input lines.
        lines (list[str]): List of strings to search in.
        search_term (str): The search term to match in each line.

    Returns:
        list[str]: List of lines that contain the search term.
    """
    search_term = search_term.lower()
    return [line for line in lines if search_term in line.lower()]


# Input
n = int(input())  # Read number of lines
lines = [input() for _ in range(n)]  # Read n lines
search_term = input()  # Read the search term

# Find and print matching lines
matching_lines = search_lines(n, lines, search_term)
print("\n".join(matching_lines))

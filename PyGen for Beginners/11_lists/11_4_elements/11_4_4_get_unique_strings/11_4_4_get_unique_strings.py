'''
TODO:
    The input to the program is a natural number n, and then n strings.
    Write a program that prints only unique strings, in the same order
    they were entered.
'''


def get_unique_strings(n: int) -> list[str]:
    """
    Reads n strings and returns a list of unique strings in the order
    they were entered.

    Args:
        n (int): The number of strings to process.

    Returns:
        list[str]: A list containing only the unique strings.
    """
    seen = set()
    unique_strings = []

    for _ in range(n):
        string = input()

        if string not in seen:
            unique_strings.append(string)
            seen.add(string)

    return unique_strings


# Input: number of strings
n = int(input())

# Get unique strings
result = get_unique_strings(n)

# Print the unique strings
print(*result, sep='\n')

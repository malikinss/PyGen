'''
TODO:
    The program receives two lines as input: one contains characters,
    the other contains a number n.

    A list is formed from the first line.

    Implement the chunked() function, which takes a list and a number
    specifying the size of a chunk as input, and returns a list of chunks
    of the specified length.
'''
from typing import List


def chunked(symbols: List[str], n: int) -> List[List[str]]:
    """
    Splits the input list into chunks of the specified size.

    Args:
        symbols (List[str]): The list to be split into chunks.
        n (int): The size of each chunk.

    Returns:
        List[List[str]]: A list of sublists where each sublist
                         is a chunk of size `n`.
    """
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result


# Input and output
symbols = input().split()  # Input symbols as a space-separated string
n = int(input())  # Input the chunk size

# Output the chunked list
print(chunked(symbols, n))

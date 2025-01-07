'''
TODO:
    Write a program to print the total number of unique characters in
    all words read, regardless of case.
'''


def count_unique_characters_in_all_words(n: int) -> int:
    """
    Counts the total number of unique characters across all words,
    ignoring case.

    Args:
        n (int): The number of words to process.

    Returns:
        int: The total number of unique characters.
    """
    given_string = ""
    for _ in range(n):
        given_string += input().lower()

    return len(set(given_string))


n = int(input())
print(count_unique_characters_in_all_words(n))

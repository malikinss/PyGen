'''
TODO:
    Write a program to print the number of unique characters of each word read
    regardless of case.
'''


def count_unique_characters(word: str) -> int:
    """
    Counts the number of unique characters in a word, ignoring case.

    Args:
        word (str): The word for which to count unique characters.

    Returns:
        int: The number of unique characters.
    """
    return len(set(word.lower()))


def process_words(n: int):
    """
    Processes multiple words and prints the number of unique characters
    for each word.

    Args:
        n (int): The number of words to process.
    """
    for _ in range(n):
        word = input()
        print(count_unique_characters(word))


# Main execution
n = int(input())
process_words(n)

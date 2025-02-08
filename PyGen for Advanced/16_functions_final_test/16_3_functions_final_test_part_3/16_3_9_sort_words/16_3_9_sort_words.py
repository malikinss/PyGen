'''
TODO:
    Given a string of space-separated words in different cases.

    Write a program that will sort the words regardless of case and then
    print them.

    The sorted words should be printed in the original case in which they were
    passed to the program as input.

NOTE:
    The built-in function sorted() sorts strings in lexicographic order,
    but is case-sensitive.

    Any uppercase letter is considered to come before a lowercase letter.
'''


def sort_words(input_string: str) -> None:
    """
    Sorts the words in the input string in lexicographic order, ignoring case,
    and prints them in the original case.

    Parameters:
    - input_string (str): A space-separated string of words to be sorted.

    Returns:
    - None: This function prints the sorted words.
    """
    words_to_sort = input_string.split()
    sorted_words = sorted(words_to_sort, key=str.lower)
    print(*sorted_words)


# Example of usage
input_string = input("Enter words to sort: ")
sort_words(input_string)

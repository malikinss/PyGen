'''
TODO:
    The input to the program is a sequence of words,
    each word on a separate line.

    The end of the sequence is one of three words:
        “stop”, “enough”, “sufficiently” (in small letters, without quotes).

    These words themselves are not included in the sequence,
    only symbolizing its end.

    Write a program that prints the total number of terms in a given sequence.
'''


def count_terms_until_keywords(keywords=None) -> int:
    """
    Counts the number of words entered until a keyword from
    'keywords' is encountered.
    Excludes the keywords themselves from the count.

    Args:
        keywords (set of str, optional): Set of keywords indicating
        the end of input.
        Defaults to {'stop', 'enough', 'sufficiently'}.

    Returns:
        int: The total count of words entered before a keyword is encountered.
    """
    if keywords is None:
        keywords = {'stop', 'enough', 'sufficiently'}

    counter = 0

    while True:
        given_word = input("Enter a word: ")
        if given_word in keywords:
            break
        counter += 1

    return counter


# Call the function and print the result
result = count_terms_until_keywords()
print(result)

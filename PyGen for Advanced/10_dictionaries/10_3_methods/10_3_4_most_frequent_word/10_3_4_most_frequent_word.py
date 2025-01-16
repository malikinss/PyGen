"""
TODO:
    Complete the code below so that it prints the most frequently occurring
    word in the string s.

    If there are multiple such words, the one that is smaller in lexicographic
    order should be printed.
"""
from typing import Dict


def most_frequent_word(s: str) -> str:
    """
    Finds the most frequently occurring word in the string `s`.
    If there are multiple such words, returns the smallest in lexicographic
    order.

    Args:
        s (str): The input string containing words separated by spaces.

    Returns:
        str: The most frequently occurring word.
    """
    words = s.split()
    word_cnts: Dict = {}

    for word in words:
        word_cnts[word] = word_cnts.get(word, 0) + 1

    max_cnt = max(word_cnts.values())
    most_common_words = []

    for word, cnt in word_cnts.items():
        if cnt == max_cnt:
            most_common_words.append(word)

    return min(most_common_words)


# Example usage
s = (
    'orange strawberry barley gooseberry apple apricot barley currant orange '
    'melon pomegranate banana banana orange barley apricot plum grapefruit '
    'banana quince strawberry barley grapefruit banana grapes melon '
    'strawberry apricot currant currant gooseberry raspberry apricot currant '
    'orange lime quince apricot currant orange lime quince grapefruit barley '
    'banana melon pomegranate barley banana orange barley apricot plum '
    'banana quince lime grapefruit strawberry gooseberry apple barley '
    'apricot currant orange melon pomegranate banana banana orange '
    'apricot barley plum banana grapefruit banana quince currant orange '
    'melon pomegranate barley plum banana quince barley lime '
    'grapefruit pomegranate barley'
)

result = most_frequent_word(s)
print(result)

'''
TODO:
    The list data contains words in Russian.

    Write a program that sorts this list in ascending order of word length.

    If the lengths of some words are the same, sort these words in
    lexicographic order.

    Sorted words should be output on one line, separated by a space.

NOTE:
    Use an anonymous function as a sorting criterion.
'''
from typing import List


def sort_russian_words(words: List[str]) -> str:
    """
    Sorts a list of Russian words in ascending order by word length.
    If words have the same length, they are sorted lexicographically.

    Args:
        words (List[str]): The list of Russian words to sort.

    Returns:
        str: A single string with the sorted words separated by a space.
    """
    sorted_words = sorted(words, key=lambda word: (len(word), word))
    return " ".join(sorted_words)


# List of Russian words
data = [
    'год', 'человек', 'время', 'дело',
    'жизнь', 'день', 'рука', 'раз',
    'работа', 'слово', 'место', 'лицо',
    'друг', 'глаз', 'вопрос', 'дом',
    'сторона', 'страна', 'мир', 'случай',
    'голова', 'ребенок', 'сила', 'конец',
    'вид', 'система', 'часть', 'город',
    'отношение', 'женщина', 'деньги'
]

# Process the data and print the result
result = sort_russian_words(data)
print(result)

# Alphabet Class

## Description 📝

The `Alphabet` class is an iterator that generates a cyclic sequence of lowercase letters based on the specified language.
The iterator can either generate letters from the English alphabet or the Russian alphabet, based on the `language` parameter passed to the constructor.

-   The English alphabet is used when the language code is `en`.
-   The Russian alphabet is used when the language code is `ru`. Note that the letter `ё` is excluded from the Russian alphabet.

## Purpose 🎯

This iterator is useful when there's a need to generate letters cyclically from either the English or Russian alphabet, such as in educational tools, games, or language-based algorithms.

## How It Works 🔍

1. **Initialization (`__init__`)**:

    - Takes one argument, `language`, which should be either 'ru' or 'en'.
    - If an unsupported language is provided, raises a `ValueError`.
    - Initializes the alphabet based on the provided language code.

2. **Iterator Protocol**:
    - `__iter__()`: Returns the iterator instance itself (`self`).
    - `__next__()`:
        - Returns the next letter in the alphabet.
        - If the end of the alphabet is reached, it loops back to the beginning of the alphabet (cyclically).

## Usage 📦

1. Save the class in a file, e.g., `alphabet.py`.
2. Create an instance for either language and iterate through the alphabet:

    ```python
    # English alphabet example
    alphabet_en = Alphabet('en')
    for letter in alphabet_en:
        print(letter)

    # Russian alphabet example
    alphabet_ru = Alphabet('ru')
    for letter in alphabet_ru:
        print(letter)
    ```

## Conclusion 🚀

The `Alphabet` iterator makes it easy to generate the lowercase letters of the English or Russian alphabet in a cyclic manner.
It is a versatile tool for applications requiring repeated letter generation, such as language games, quizzes, or algorithms based on alphabetic characters.

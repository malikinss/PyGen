# Wordplay Class Word Filter

## Description 📝

The `Wordplay` class manages an extensible set of unique words, initialized with an optional list of words (defaulting to empty).
It provides methods to add words (ignoring duplicates), and filter the set by length, allowed letters, or forbidden letters, preserving the order of addition.
The class ensures independence from the initial list by creating a copy during instantiation.

## Purpose 🎯

This class is designed for word manipulation and filtering tasks, making it ideal for educational exercises, word games, or linguistic analysis where specific word properties need to be queried while maintaining insertion order.

## How It Works 🔍

-   **Initialization**: The `__init__` method creates a copy of the provided `words` list or an empty list if none is given.
-   **add_word() Method**: Adds a word to the `words` list only if it’s not already present.
-   **words_with_length() Method**: Returns words of a specified length `n`.
-   **only() Method**: Filters words that consist solely of given letters using a set-based check.
-   **avoid() Method**: Filters words that contain none of the given letters.
-   **Helper Method**: `_is_word_made_of_letters()` checks if a word uses only allowed letters.

## Output 📜

Example usage:

```python
wp = Wordplay(["cat", "dog"])
wp.add_word("rat")
wp.add_word("cat")  # Ignored (duplicate)
print(wp.words_with_length(3))      # Output: ['cat', 'dog', 'rat']
print(wp.only("c", "a", "t"))       # Output: ['cat']
print(wp.avoid("r", "d"))           # Output: ['cat']
```

## Usage 📦

1. Save the class in a Python file, e.g., `wordplay.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from wordplay import Wordplay
my_words = Wordplay(["apple", "pie"])
my_words.add_word("pea")
print(f"Length 3: {my_words.words_with_length(3)}")  # Output: Length 3: ['pie', 'pea']
print(f"Only p,e,a: {my_words.only('p', 'e', 'a')}")  # Output: Only p,e,a: ['pea']
print(f"Avoid l: {my_words.avoid('l')}")             # Output: Avoid l: ['pie', 'pea']
```

## Conclusion 🚀

The `Wordplay` class offers a flexible and efficient way to manage and filter a set of words based on length or letter constraints in Python.
Its preservation of order and handling of uniqueness make it a robust tool for word-based applications, easily extensible with additional filtering criteria or case sensitivity options for broader use cases.

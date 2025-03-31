# TextHandler Class Word Manager

## Description 📝

The `TextHandler` class manages an extensible collection of words extracted from text.
It starts empty, allows adding words from text input, and provides methods to retrieve the shortest and longest words in the order they were added.
The class uses regular expressions to identify words (sequences of letters) and requires no arguments upon instantiation.

## Purpose 🎯

This class is designed to process and analyze text by collecting words and identifying those with minimum or maximum lengths, making it useful for text processing exercises, linguistic analysis, or educational demonstrations of list filtering and order preservation.

## How It Works 🔍

-   **Initialization**: The `__init__` method creates an empty list `words` to store the collection.
-   **add_words() Method**: Extracts words from text using regex (`\b[a-zA-Zа-яА-ЯёЁ]+\b`) and appends them to the `words` list.
-   **get_shortest_words() Method**: Returns all words with the minimum length, preserving their original order, or an empty list if the collection is empty.
-   **get_longest_words() Method**: Returns all words with the maximum length, preserving their original order, or an empty list if the collection is empty.
-   **Helper Methods**: Internal methods calculate word lengths and filter the list based on target lengths.

## Output 📜

Example usage:

```python
handler = TextHandler()
handler.add_words("cat dog elephant bird")
print(handler.get_shortest_words())  # Output: ['cat', 'dog']
print(handler.get_longest_words())   # Output: ['elephant']
handler.add_words("rat lion")
print(handler.get_shortest_words())  # Output: ['cat', 'dog', 'rat']
print(handler.get_longest_words())   # Output: ['elephant']
```

## Usage 📦

1. Save the class in a Python file, e.g., `text_handler.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from text_handler import TextHandler
text = TextHandler()
text.add_words("apple banana cherry date")
print(f"Shortest: {text.get_shortest_words()}")  # Output: Shortest: ['date']
print(f"Longest: {text.get_longest_words()}")    # Output: Longest: ['banana', 'cherry']
```

## Conclusion 🚀

The `TextHandler` class provides a robust and flexible way to manage a collection of words, efficiently identifying the shortest and longest ones while maintaining their insertion order.
Its use of regex and filtering makes it adaptable to various text inputs, and it can be enhanced with features like case sensitivity options or word frequency tracking for more advanced text analysis tasks.

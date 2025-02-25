# Extracting Fifth Letters with Error Handling 📝

## Description 📝

The function extracts the fifth letter from each word in the `food` list.
If a word has fewer than five letters, `_` is added instead.
A `try-except` block ensures the program does not crash due to `IndexError`.

## Purpose 🎯

To process a list of food names and extract their fifth letter while handling words that are too short.

## How It Works 🔍

1. The function iterates through the `food` list.
2. It tries to access the fifth letter (index `4`).
3. If the word is too short, an `IndexError` occurs, and `_` is added instead.
4. The extracted letters are stored in a new list and returned.

## Output 📜

**Example Input:**

```python
food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
```

**Example Output:**

```python
['l', 'e', '_', 'w', '_', 't', '_', '_', 'n']
```

## Usage 📦

1. Call `extract_fifth_letters(food)` with a list of food items.
2. The function will return a list of fifth letters or `_` for short words.

## Conclusion 🚀

The function now safely extracts the fifth letter from words while handling short words gracefully.

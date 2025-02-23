# Scrabble Word Validator

## Description 📝

This Python function determines whether a given word can be formed using a set of available symbols, considering the number of occurrences of each letter.
The check is case-insensitive.

## Purpose 🎯

The function helps validate if a word can be constructed using a limited set of characters, which can be useful in games like Scrabble, word puzzles, or text-based challenges.

## How It Works 🔍

1. The function takes two arguments:

    - `symbols`: A string representing available characters.
    - `word`: The target word to be formed.

2. It counts the occurrences of each letter in both `symbols` and `word`.

3. The function verifies whether the `symbols` contain at least as many occurrences of each letter as needed to construct the `word`.

4. If all characters in the `word` are available in sufficient quantity, the function returns `True`; otherwise, it returns `False`.

## Output 📜

The function returns a boolean:

-   `True` if the word can be formed from the given symbols.
-   `False` otherwise.

### Example:

#### Function Calls and Expected Results:

```python
print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))  # Expected: True
print(scrabble('begk', 'beegeek'))  # Expected: False
```

## Usage 📦

1. Import or define the `scrabble()` function in your Python script.
2. Call the function with the required parameters.
3. Process the boolean result as needed.

### Running the function:

```python
result = scrabble('abcdefg', 'face')
print(result)  # Expected: True
```

## Conclusion 🚀

This function is a simple and efficient way to check if a word can be formed from a given set of letters.
It is useful for word games, educational applications, and natural language processing tasks.

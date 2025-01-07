# Same Letter Set Checker Program 🔤

## Description 📝

This program takes a string consisting of three words as input and determines whether the same set of letters was used to write all three words.
The order and frequency of letters do not matter, only the unique set of letters in each word is considered.

## Purpose 🎯

-   To check if all three words in the input consist of the same unique set of letters.
-   To demonstrate how to use sets in Python to compare the unique characters in multiple strings.

## How It Works 🔍

1. **Function `same_letter_set`**:

    - Accepts a list `words` containing exactly three words.
    - Converts the first word into a set of letters (`first_word_set`).
    - Uses the `all()` function to check if all the other words have the same set of letters as the first word.
        - For each word, the set of letters is compared with `first_word_set`.
    - If all words have the same set of letters, the function returns `"YES"`.
    - Otherwise, it returns `"NO"`.

2. **Input**:

    - A string of three words is taken as input, split by spaces into a list.

3. **Output**:
    - The program outputs `"YES"` if all three words contain the same set of unique letters, otherwise it outputs `"NO"`.

### Example:

```python
words = ["abc", "cab", "bca"]
print(same_letter_set(words))
```

**Output**:

```
YES
```

```python
words = ["hello", "world", "hey"]
print(same_letter_set(words))
```

**Output**:

```
NO
```

## Output 📜

-   If the input is `"abc cab bca"`, the output will be `"YES"` because all three words contain the same letters: `a`, `b`, and `c`.
-   If the input is `"hello world hey"`, the output will be `"NO"` because the sets of letters in the words are different.

## Conclusion 🚀

This program effectively checks if three words consist of the same set of unique letters using Python's set data structure, ignoring the order and frequency of the letters.

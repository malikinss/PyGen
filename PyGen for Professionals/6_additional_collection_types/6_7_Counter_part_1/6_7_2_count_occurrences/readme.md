# Count Occurrences of a Word in a Sequence of Words

## Description 📝

This Python program defines a function `count_occurrences` that counts how many times a specified word appears in a sequence of words, ignoring case differences.
It returns the number of occurrences.

## Purpose 🎯

The purpose of this function is to count the occurrences of a specific word in a string of words, handling case insensitivity.
This can be useful for text analysis, word frequency counting, or other similar tasks.

## How It Works 🔍

1. The function `count_occurrences` takes two arguments:
    - `word`: A string representing the word to count.
    - `words`: A string of space-separated words.
2. The function converts both the target word and the sequence of words to lowercase to make the comparison case-insensitive.
3. It counts how many times the word appears in the sequence of words and returns that number.

## Output 📜

The function returns an integer representing the number of occurrences of the specified word.

### Example 1:

Input:

```python
word = 'python'
words = 'Python Conferences python training python events'
```

Output:

```
3
```

### Example 2:

Input:

```python
word = 'Java'
words = 'Python C++ C# JavaScript Go Assembler'
```

Output:

```
0
```

## Usage 📦

1. Copy the code into your Python file.
2. Call the function `count_occurrences(word, words)` with the word and sequence you want to analyze.

### Example:

```python
word = 'python'
words = 'Python Conferences python training python events'
print(count_occurrences(word, words))
```

## Conclusion 🚀

The `count_occurrences` function provides an easy way to count word occurrences in a case-insensitive manner.
It's a helpful tool for simple text analysis and processing.

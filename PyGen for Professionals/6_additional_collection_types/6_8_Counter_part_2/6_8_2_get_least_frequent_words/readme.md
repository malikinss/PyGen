# Least Frequently Occurring Words Finder

## Description 📝

This Python program takes a sequence of words as input and identifies the least frequently occurring word(s).
If multiple words share the lowest frequency, the program outputs them in lexicographic order, separated by a comma and a space.

## Purpose 🎯

The program helps analyze word frequency in a given sequence and provides insight into which words appear the least.
It processes input text, counts occurrences, and determines the words with the lowest frequency.

## How It Works 🔍

1. The user inputs a sequence of words separated by spaces.
2. The program converts all words to lowercase.
3. It counts the frequency of each word using Python’s `Counter` from the `collections` module.
4. The word(s) with the lowest frequency are identified.
5. If multiple words have the same lowest frequency, they are sorted lexicographically and displayed.

## Output 📜

The program prints the least frequently occurring word(s) in lowercase.

### Example 1:

#### Input:

```
Python Java C++ python Java Ruby Go
```

#### Processing:

-   Converted to lowercase: `["python", "java", "c++", "python", "java", "ruby", "go"]`
-   Word counts:
    -   `"python": 2`
    -   `"java": 2`
    -   `"c++": 1`
    -   `"ruby": 1`
    -   `"go": 1`
-   Least frequent words: `["c++", "go", "ruby"]` (sorted lexicographically)

#### Output:

```
c++, go, ruby
```

### Example 2:

#### Input:

```
apple banana apple orange banana grape
```

#### Output:

```
grape, orange
```

## Usage 📦

1. Run the script.
2. Enter a sequence of words separated by spaces.
3. The program will output the least frequently occurring words in lowercase, sorted lexicographically.

### Example:

```python
# User input:
apple banana apple orange banana grape

# Program output:
grape, orange
```

## Conclusion 🚀

This program efficiently finds the least frequently occurring words in a sequence while ignoring case differences.
It ensures accurate counting and sorting using Python’s built-in `Counter` and `sorted()` functions.

# Most Frequently Occurring Word Finder

## Description 📝

This Python program takes a sequence of words as input and identifies the most frequently occurring word.
If multiple words share the highest frequency, the program outputs the lexicographically greatest word in lowercase.

## Purpose 🎯

The program processes an input text sequence, counts word occurrences, and determines the most frequent word, prioritizing lexicographic order in case of ties.
This is useful for text analysis and data processing.

## How It Works 🔍

1. The user inputs a sequence of words separated by spaces.
2. The program converts all words to lowercase.
3. It counts word occurrences using Python’s `Counter` from the `collections` module.
4. The word(s) with the highest frequency are identified.
5. If multiple words have the same highest frequency, the lexicographically greatest one is chosen.

## Output 📜

The program prints the most frequently occurring word in lowercase.

### Example 1:

#### Input:

```
apple banana apple orange banana grape banana
```

#### Processing:

-   Converted to lowercase: `["apple", "banana", "apple", "orange", "banana", "grape", "banana"]`
-   Word counts:
    -   `"apple": 2`
    -   `"banana": 3`
    -   `"orange": 1`
    -   `"grape": 1`
-   Most frequent word: `"banana"` (appears 3 times)

#### Output:

```
banana
```

### Example 2 (Tie Case):

#### Input:

```
cat dog elephant dog elephant
```

#### Processing:

-   Converted to lowercase: `["cat", "dog", "elephant", "dog", "elephant"]`
-   Word counts:
    -   `"cat": 1`
    -   `"dog": 2`
    -   `"elephant": 2`
-   Tie between `"dog"` and `"elephant"`, lexicographically greater is `"elephant"`.

#### Output:

```
elephant
```

## Usage 📦

1. Run the script.
2. Enter a sequence of words separated by spaces.
3. The program will output the most frequently occurring word in lowercase.
4. In case of a tie, the lexicographically greatest word will be displayed.

### Example:

```python
# User input:
apple banana apple orange banana grape banana

# Program output:
banana
```

## Conclusion 🚀

This program efficiently finds the most frequently occurring word in a sequence while ensuring case insensitivity.
It accurately resolves ties using lexicographic order, making it useful for text analysis tasks.

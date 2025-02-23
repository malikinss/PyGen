# Word Length Grouping Program

## Description 📝

This Python program takes a sequence of words as input and groups them based on their length.
It then counts the number of words in each group and outputs the results in ascending order of group size.
If multiple groups have the same size, the order is determined by the first occurrence of a word from that group in the input.

## Purpose 🎯

The program processes an input string, groups words by their length, and displays the number of words in each group.
This is useful for text analysis, word categorization, and frequency distribution studies.

## How It Works 🔍

1. The user enters a sequence of words separated by spaces.
2. The program converts all words to lowercase.
3. It groups words by their length using a dictionary (`defaultdict`).
4. The program counts the words in each group.
5. Groups are sorted by the number of words in ascending order.
6. The results are printed in the required format.

## Output 📜

Each group is represented in the format:

```
Words of length <length>: <count>
```

### Example 1:

#### Input:

```
apple banana cat dog elephant hi no to is
```

#### Processing:

-   Converted to lowercase: `["apple", "banana", "cat", "dog", "elephant", "hi", "no", "to", "is"]`
-   Grouped by length:
    -   Length `2`: `["hi", "no", "to", "is"]` → Count: `4`
    -   Length `3`: `["cat", "dog"]` → Count: `2`
    -   Length `5`: `["apple"]` → Count: `1`
    -   Length `6`: `["banana"]` → Count: `1`
    -   Length `8`: `["elephant"]` → Count: `1`
-   Sorted by group size in ascending order.

#### Output:

```
Words of length 5: 1
Words of length 6: 1
Words of length 8: 1
Words of length 3: 2
Words of length 2: 4
```

## Usage 📦

1. Run the script.
2. Enter a sequence of words separated by spaces.
3. The program will output the number of words in each group, sorted by size.

### Example:

```python
# User input:
apple banana cat dog elephant hi no to is

# Program output:
Words of length 5: 1
Words of length 6: 1
Words of length 8: 1
Words of length 3: 2
Words of length 2: 4
```

## Conclusion 🚀

This program efficiently groups words by their length and presents the results in an organized manner, making it useful for linguistic analysis and text-based data categorization.

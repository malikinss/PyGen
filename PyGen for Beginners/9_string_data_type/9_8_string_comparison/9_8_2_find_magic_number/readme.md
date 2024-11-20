# Magic Number Finder 📝

## Description 📝

This program calculates a "magic" number based on a set of 4 words provided as input.
The "magic" number is determined by the following steps:

1. Find the lexicographically smallest and largest words in the set.
2. Multiply the Unicode code points of the last characters of these words.
3. Square the resulting product.

The program outputs the final calculated "magic" number.

## Purpose 🎯

The purpose of this program is to demonstrate how to calculate a "magic" number based on string comparisons and character Unicode values.
It processes exactly 4 input words and calculates the magic number using the algorithm described.

## How It Works 🔍

1. The program reads 4 words from the input.
2. It finds the lexicographically smallest and largest words.
3. The Unicode values of the last characters of these words are multiplied, and the result is squared to get the magic number.
4. Finally, the magic number is printed as output.

### Example

```bash
Input:
cat
apple
banana
dog

Output:
282024
```

### Explanation:

-   Smallest word: "apple" (last character: "e", Unicode code: 101)
-   Largest word: "dog" (last character: "g", Unicode code: 103)
-   Magic number: `(101 * 103) ** 2 = 282024`

## Usage 📦

1. Copy the program code into a Python script file (e.g., `magic_number.py`).
2. Run the script in your terminal or an IDE.
3. Enter 4 words, each on a new line.
4. The program will output the calculated magic number.

## Conclusion 🚀

This program provides a fun way to calculate a "magic" number from a set of words based on their lexicographic order and the Unicode values of their last characters.
It's an interesting application of string manipulation and Unicode in Python.

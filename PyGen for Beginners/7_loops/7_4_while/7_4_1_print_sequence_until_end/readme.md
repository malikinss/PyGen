# Sequence Printer Until "END"

## Description 📝

This program reads a sequence of words from the user, one per line, and stops reading when the word "END" is entered.
The program prints each word in the sequence, excluding "END" itself, which only marks the end of input.

## Purpose 🎯

The purpose of this program is to demonstrate how to process and display a sequence of user-provided inputs until a specific stopping condition is met.
This is useful for scenarios where data entry continues until a specific "terminator" is given.

## How It Works 🔍

1. The program enters a loop that continues to read words from the user.
2. Each word is immediately printed after being entered.
3. If the word "END" is entered, the loop breaks and stops further processing.
4. The word "END" is not printed, as it only serves as a stopping signal.

## Output 📜

The program outputs each word entered by the user until "END" is reached.

Examples:

### Example 1

```bash
Input: hello world END
Output: hello world
```

### Example 2

```bash
Input: apple banana cherry END
Output: apple banana cherry
```

## Usage 📦

1. Run the script in a Python environment.
2. Enter words one by one; each word will be printed immediately.
3. To stop entering words, type "END".
4. The program will output each word entered before "END".

## Conclusion 🚀

This program effectively reads and prints a sequence of words, allowing for easy data entry and processing with a specified stopping word.

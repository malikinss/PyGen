# Sequence Printer Until "END" or "end"

## Description 📝

This program reads a sequence of words entered by the user, stopping when either `"END"` or `"end"` is entered.
It prints each word in the sequence, excluding the keywords `"END"` and `"end"` themselves, which only indicate the end of the sequence.

## Purpose 🎯

This program is designed to process and display user-inputted words until specific keywords are given.
It demonstrates how to use a custom stopping condition based on multiple keyword options.

## How It Works 🔍

1. The program enters a loop to continuously read words from the user.
2. Each word is printed immediately after it’s entered.
3. If the word matches any keyword from the set `{'END', 'end'}`, the loop breaks.
4. The program only prints words in the sequence before these keywords, excluding the keywords themselves.

## Output 📜

The program outputs each word entered by the user until either `"END"` or `"end"` is inputted.

### Example 1

```bash
Input: apple banana END
Output: apple banana

```

### Example 2

```bash
Input: first second third end
Output: first second third

```

## Usage 📦

1. Run the script in a Python environment.
2. Enter words one by one. Each word will be printed immediately after being entered.
3. To stop entering words, type either `"END"` or `"end"`.
4. The program will output each word entered prior to the stopping keyword.

## Conclusion 🚀

This program enables sequence input and output, stopping at predefined keywords, and is flexible to allow multiple stopping options.

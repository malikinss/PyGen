# Get Unique Strings 📝

## Description 📝

This Python program takes a list of strings as input and returns only the unique strings, preserving the order in which they were entered. Duplicate strings are ignored and not printed again.

## Purpose 🎯

The program helps in scenarios where we need to filter out duplicate entries from a list of strings while keeping the order of the first occurrence intact. This can be useful in data processing, handling user inputs, or analyzing text data where duplicates need to be removed.

## How It Works 🔍

1. The program first reads an integer `n` which specifies the number of strings to be entered.
2. It then reads `n` strings one by one.
3. The program keeps track of the strings that have already been seen using a set, ensuring that only the first occurrence of each string is added to the result list.
4. Finally, the program outputs the unique strings, one per line, in the order they were entered.

## Output 📜

```bash
Example Input:
5
apple
banana
apple
orange
banana

Example Output:
apple
banana
orange
```

## Usage 📦

1. Save the script as `get_unique_strings.py`.
2. Run the script in a Python environment.
3. Input the number `n` (number of strings to be entered).
4. Input `n` strings, one per line.
5. The program will output the unique strings, each on a separate line.

## Conclusion 🚀

This program provides a simple and efficient way to filter out duplicate strings while preserving the original order, making it a useful tool for data cleaning and processing.

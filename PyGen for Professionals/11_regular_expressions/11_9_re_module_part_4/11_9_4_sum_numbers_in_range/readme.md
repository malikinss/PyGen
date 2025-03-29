# Sum Numbers in Range 🔢

## Description 📝

This program extracts **natural numbers** from a given string within a specified **index range** and returns their sum.
If there are no numbers within the range, it outputs 0.

## Purpose 🎯

The goal is to process a string, find all natural numbers in a specific range of indices, and sum them.
This can be helpful in text parsing, data extraction, and filtering based on specific index ranges.

## How It Works 🔍

1. **Input**:

    - The program takes two integers (`a` and `b`) which represent the starting and ending indices (inclusive and exclusive, respectively).
    - A string is then provided that may contain natural numbers.

2. **Regex Extraction**:

    - The program uses regular expressions to find all **natural numbers** (sequences of digits) within the specified range of indices.

3. **Summing Numbers**:
    - It sums up all the numbers found in the range and outputs the result.

## Output 📜

### Example Input:

```sh
2 12
The number 100 is between 2 and 12.
```

### Example Output:

```sh
100
```

## Usage 📦

1. Run the script:
    ```sh
    python sum_numbers_in_range.py
    ```
2. Input two integers for the index range (e.g., `2 12`).
3. Enter the string containing numbers (e.g., `The number 100 is between 2 and 12.`).
4. The output will display the sum of the numbers within the range:
    ```sh
    100
    ```

## Conclusion 🚀

This program efficiently sums **natural numbers** found in a given range of indices within a string.
It’s useful for parsing numeric data from structured text.

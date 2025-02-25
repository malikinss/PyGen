# Summing Numeric Inputs and Counting Non-Numeric Values 📝

## Description 📝

The program reads multiple lines of input, separates numeric values from non-numeric values, computes the sum of all numbers, and counts the non-numeric inputs.

## Purpose 🎯

To correctly process an unspecified number of input lines, handling numeric and non-numeric values separately.

## How It Works 🔍

1. **Reading Input**: Uses `sys.stdin.readlines()` to capture multiple lines.
2. **Processing Data**:
    - Converts valid numbers to `float`.
    - Stores non-numeric values separately.
3. **Computing and Formatting Output**:
    - Prints the sum of all numeric values (as `int` if there are no decimals).
    - Prints the count of non-numeric inputs.

## Output 📜

**Example Input:**

```
10
abc
5.5
xyz
20
```

**Example Output:**

```
35.5
2
```

## Usage 📦

1. Run the script and enter values line by line.
2. The program will sum numbers and count non-numeric inputs.

## Conclusion 🚀

This approach ensures correct number parsing and robust error handling while maintaining readable output.

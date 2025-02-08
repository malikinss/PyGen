# Program to Calculate the Sum of All Numbers in a Text File 📝💰

## Description 📝

This program reads a file **"nums.txt"** that contains non-negative integers mixed with other text. It extracts all numbers from the file and calculates their sum.

## Purpose 🎯

To extract all non-negative integers from a text file and compute the sum of these numbers, ignoring other content.

## How It Works 🔍

1. **Reading File (`get_data_from_file`)**:

    - The file **"nums.txt"** is opened and read line by line.
    - Each line is stored in a list for further processing.

2. **Extracting Numbers (`extract_numbers_from_text`)**:

    - The program uses regular expressions (`\d+`) to identify sequences of digits (representing non-negative integers) in each line.
    - These numbers are extracted and converted to integers using `map(int, ...)`.
    - All extracted numbers are gathered into a single list.

3. **Calculating the Sum**:

    - The sum of all extracted numbers is calculated using Python's built-in `sum()` function.

4. **Outputting Results**:
    - The total sum of the numbers is displayed to the user.

## Example Usage:

**File (`nums.txt`):**

```
The price is 50
There are 100 apples
Total: 150
No numbers here!
```

**Program Output:**

```python
>>> 300
```

## Conclusion 🚀

This program effectively extracts and sums up all the numbers present in a text file. It handles mixed content and non-digits gracefully, providing the correct result based on the numbers in the file.

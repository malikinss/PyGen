# Palindrome Numbers from 100 to 1000

## Description 📝

This Python script generates a list of **palindrome numbers** between 100 and 1000.
A **palindrome** is a number that reads the same forward and backward, such as `121` or `545`.

## Purpose 🎯

-   To practice **list comprehensions** for generating filtered lists based on conditions.
-   Implement a concise solution to identify palindrome numbers within a specific range.
-   Demonstrate the manipulation of integers as strings to check for palindromic properties.

## How It Works 🔍

1. **Function Definition**:  
   The function `find_palindromes` returns a list of numbers between 100 and 1000.
2. **Palindrome Check**:  
   A number is converted to a string and compared to its reverse (`str(i)[::-1]`). If they match, the number is a palindrome.
3. **List Comprehension**:  
   The list comprehension iterates over the range of numbers from 100 to 1000 and filters only palindromic numbers.
4. **Execution**:  
   The resulting list is printed.

### Key Points:

-   **Efficiency**: List comprehension allows for quick filtering in one line.
-   **String Manipulation**: Reversing a string using slicing (`[::-1]`) is an elegant way to check for palindromes.
-   **Range**: The code checks numbers from 100 to 1000 (inclusive).

## Output 📜

The script outputs a list of all three-digit palindrome numbers.

**Example Output:**

```
[101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999]
```

## Usage 📦

1. Copy the code into a Python file, e.g., `palindrome_numbers.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python palindrome_numbers.py
    ```
5. The list of palindromic numbers will be displayed.

## Conclusion 🚀

This script efficiently identifies three-digit palindromic numbers using **Python's list comprehension** and **string manipulation techniques**.
It highlights how compact and readable code can perform powerful operations with minimal lines. 🌟

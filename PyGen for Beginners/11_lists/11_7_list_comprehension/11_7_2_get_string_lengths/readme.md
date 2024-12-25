# Get String Lengths from List

## Description 📝

This Python script calculates the length of each string in a list using **list comprehension** and returns a new list of integers representing the lengths.
It efficiently processes the list and outputs the size of each string.

## Purpose 🎯

The main objectives of the program are:

-   Demonstrate the use of **list comprehensions** to perform operations on lists in a concise and readable manner.
-   Calculate the length of each string in a given list of Python keywords.
-   Return the list of lengths as output.

## How It Works 🔍

1. **Function Definition**:  
   The function `get_string_lengths` accepts a list of strings.
2. **List Comprehension**:  
   The function iterates over each string in the list, calculates its length using `len()`, and stores the result in a new list.
3. **Execution**:  
   The function is applied to a list of Python keywords, and the resulting list of lengths is printed.

### Key Points:

-   **Efficiency**: The list comprehension allows for a one-liner solution to iterate over the list and apply the length calculation.
-   **Simplicity**: Compared to traditional loops, this method is more concise and easier to read.

## Output 📜

The program outputs a list of integers representing the length of each string in the list.

**Example Output:**

```
[5, 4, 4, 3, 4, 2, 6, 5, 5, 8, 3, 3, 4, 4, 6, 7, 3, 2, 4, 6, 2, 6, 2, 2, 6, 8, 3, 2, 4, 5, 6, 6, 5]
```

## Usage 📦

1. Copy the code into a file named `get_string_lengths.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python get_string_lengths.py
    ```
5. The list of string lengths will be printed in the terminal.

## Conclusion 🚀

By using **list comprehensions**, the program efficiently processes lists and returns meaningful results with minimal code.
This simple yet effective example highlights Python's capability to handle list transformations elegantly and powerfully.
Mastering such techniques improves code quality and readability. 🌟

# Sum of Corresponding Elements in Lists

## Description 📝

This Python program takes two lines of integers as input, forming two lists `L` and `M`.
It then creates a third list, where each element is the sum of the corresponding elements from `L` and `M`. Finally, the program prints each element of the resulting list on a single line, separated by spaces.

## Purpose 🎯

-   To perform element-wise addition of two lists of integers.
-   To practice working with lists and manipulating their elements in Python.

## How It Works 🔍

1. **Function `sum_lists`**:

    - Takes two lists of integers, `lst1` and `lst2`, as input.
    - Uses a list comprehension to sum the corresponding elements from both lists.
    - The resulting list is returned, which contains the sums of the corresponding elements.

2. **User Input**:

    - The program first reads two lines of integers from the user.
    - These integers are split into individual numbers and converted into two lists `line1` and `line2`.

3. **Result Calculation**:

    - The `sum_lists` function is called with `line1` and `line2` as arguments.
    - The program then calculates the sums of the corresponding elements and stores them in the `result` list.

4. **Output**:
    - The program prints the elements of the `result` list on a single line, separated by spaces.

## Output 📜

The program prints the sum of the corresponding elements of the two lists, each on one line, separated by spaces.

**Example 1**:

```
Input:
1 2 3
4 5 6

Output:
5 7 9
```

**Example 2**:

```
Input:
10 20 30
1 2 3

Output:
11 22 33
```

## Usage 📦

1. Copy the code into a Python file, e.g., `sum_lists.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python sum_lists.py
    ```
5. Enter two lines of space-separated integers.
6. View the sums of the corresponding elements printed on a single line.

## Conclusion 🚀

This program efficiently calculates the sum of corresponding elements from two lists and demonstrates basic list operations in Python.
It's a great example of handling user input and manipulating lists. 🎉

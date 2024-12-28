# Sum of Numbers with "+" Sign

## Description 📝

This Python program takes a text string of natural numbers separated by spaces, inserts a "+" sign between each number, and calculates the sum of the numbers.
The output displays the numbers in the format `number1+number2+...=sum`, where `sum` is the sum of all the numbers.

## Purpose 🎯

-   To practice string manipulation, list handling, and basic arithmetic operations in Python.
-   To demonstrate formatting and output techniques using `print` statements.

## How It Works 🔍

1. **User Input**:

    - The program accepts a single string of space-separated natural numbers as input.

2. **String Manipulation**:

    - The input string is split into individual numbers using the `split()` function, then each number is converted into an integer.

3. **Sum Calculation**:

    - The program calculates the sum of all the numbers using Python's built-in `sum()` function.

4. **Output Formatting**:
    - The program prints the numbers with a "+" sign between them using `print(*numbers, sep='+')`.
    - It then appends the sum after an equals sign (`=`), completing the output format.

## Output 📜

The program prints the numbers with "+" signs separating them, followed by the total sum.

**Example 1**:

```
Input:
1 2 3 4

Output:
1+2+3+4=10
```

**Example 2**:

```
Input:
5 10 15 20

Output:
5+10+15+20=50
```

## Usage 📦

1. Copy the code into a Python file, e.g., `sum_numbers.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python sum_numbers.py
    ```
5. Enter a space-separated string of natural numbers when prompted.
6. View the output in the format `number1+number2+...=sum`.

## Conclusion 🚀

This program demonstrates how to manipulate strings, process numbers, and format output in Python.
It's a great example of handling user input and performing basic arithmetic operations. 🎉

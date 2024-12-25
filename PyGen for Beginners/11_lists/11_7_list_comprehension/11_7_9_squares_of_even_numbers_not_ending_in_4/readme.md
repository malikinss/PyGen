# Squares of Even Numbers Not Ending in 4

## Description 📝

This Python program takes an input string containing space-separated integers and computes the squares of even numbers that do not end in the digit '4'.
The results are printed on the same line.

## Purpose 🎯

-   To practice filtering integers based on specific criteria (even numbers that do not end in '4').
-   To demonstrate list comprehension in Python for transforming and filtering data.
-   To handle user input and display the computed results.

## How It Works 🔍

1. **Function `squares_of_even_numbers_not_ending_in_4`**:

    - Accepts a string `text` containing space-separated integers.
    - Splits the string into a list of numbers.
    - Uses a list expression to:
        - Convert each number to an integer.
        - Check if the number is even (`i % 2 == 0`).
        - Ensure that the number does not end with '4' (`i[-1] != '4'`).
    - If both conditions are satisfied, the square of the number is added to the result list.

2. **Function `main`**:
    - Prompts the user to input a string of space-separated integers using `input()`.
    - Calls the `squares_of_even_numbers_not_ending_in_4` function to get the list of squared numbers.
    - Prints the results as a space-separated list on the same line.

## Output 📜

The program prints the squares of the even numbers that do not end in '4', in the order they appeared in the input.

**Example**:

```
Enter space-separated integers: 12 14 16 18 24 34 36
144 324 1296 1156
```

## Usage 📦

1. Copy the code into a Python file, e.g., `squares_even_numbers.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python squares_even_numbers.py
    ```
5. Enter a string of space-separated integers when prompted.
6. View the squares of even numbers that do not end in 4, printed on the same line.

## Conclusion 🚀

This program efficiently computes the squares of even numbers that do not end in 4 from a string of integers.
It is a great example of using list comprehension to filter and transform data in Python. 🎉

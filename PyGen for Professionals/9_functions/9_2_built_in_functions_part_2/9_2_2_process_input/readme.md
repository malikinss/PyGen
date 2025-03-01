# Process Input Program

## Description 📝

This Python script processes input data provided as a string, which represents a list, tuple, or set.
Depending on the type of the input, the program performs specific operations:

-   If the input is a list, it outputs the last element.
-   If the input is a tuple, it outputs the first element.
-   If the input is a set, it outputs the number of elements in the set.

## Purpose 🎯

The goal of this program is to demonstrate how to handle different data types (list, tuple, set) and perform operations based on the type of the input.
It also highlights the use of the `eval()` function to convert string representations of data structures into their corresponding Python objects.

## How It Works 🔍

1. **process_input() Function**:
    - Takes a string input that represents a list, tuple, or set.
    - Uses `eval()` to convert the string to the corresponding Python data structure.
    - Based on the type of the data (list, tuple, or set), it performs the respective operation.
2. **Operations Dictionary**: A dictionary maps data types to corresponding lambda functions:

    - **list**: Outputs the last element using `x[-1]`.
    - **tuple**: Outputs the first element using `x[0]`.
    - **set**: Outputs the number of elements using `len(x)`.

3. **Error Handling**:
    - If the string doesn't represent a valid list, tuple, or set, a `ValueError` is raised.
    - If the data type is unsupported, a `TypeError` is raised.

## Output 📜

When the script is executed with the following inputs:

-   `process_input("[1, 2, 3]")`, the output will be:
    ```
    3
    ```
-   `process_input("(1, 2, 3)")`, the output will be:
    ```
    1
    ```
-   `process_input("{1, 2, 3}")`, the output will be:
    ```
    3
    ```

## Usage 📦

1. Save the code to a file named `process_input.py`.
2. Provide the input data as a string representing a valid list, tuple, or set.
3. Open a terminal or command prompt.
4. Navigate to the directory where the file is located.
5. Execute the script using the command:
    ```
    python process_input.py
    ```
6. The program will display the result based on the input data.

## Conclusion 🚀

This program demonstrates how to handle different data types and perform type-specific operations.
It also teaches the use of `eval()` for dynamically interpreting string inputs as Python objects.

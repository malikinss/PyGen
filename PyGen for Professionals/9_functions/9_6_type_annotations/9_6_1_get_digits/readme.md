# Get Digits

## Description 📝

This Python script defines the `get_digits()` function, which extracts the digits from a given positive integer or float and returns them as a list of integers.
The order of the digits in the list matches the order of their occurrence in the original number.

## Purpose 🎯

The purpose of this program is to provide a way to extract all digits from a number (whether integer or float) and return them in the form of a list.
The function handles both integer and floating-point inputs while maintaining the order of the digits.

## How It Works 🔍

1. **Input**: The function takes one argument:
    - `number`: A positive integer or float from which to extract digits.
2. **Input Validation**: The function raises a `ValueError` if the `number` is negative.
3. **String Conversion**: The function converts the `number` to a string to easily access individual digits.
4. **Digit Extraction**: It iterates through each character of the string, checks if it's a digit (ignoring the decimal point in case of floats), and adds it to the result list as an integer.
5. **Output**: The function returns a list of integers, where each integer is a digit from the original number.

## Output 📜

For a given input number, the output will be a list of digits.  
For example:

```python
get_digits(123.456)
```

The output will be:

```python
[1, 2, 3, 4, 5, 6]
```

## Usage 📦

1. Save the code to a file named `get_digits.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```python
    python get_digits.py
    ```
5. Call the function `get_digits()` with a positive integer or float.
   Example:
    ```python
    number = 987.654
    digits = get_digits(number)
    print(digits)  # Output: [9, 8, 7, 6, 5, 4]
    ```

## Conclusion 🚀

This function provides a simple and efficient way to extract digits from a number, whether it's an integer or a floating-point number.
It is a useful utility for number manipulation in Python.

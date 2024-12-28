# Number of Factors Program 🔢

## Description 📝

This Python program calculates the number of factors of a given natural number.
It utilizes the `get_factors` function to determine all factors and returns the count of these factors.

## Purpose 🎯

-   To find how many factors a number has.
-   Helpful in number theory, mathematical problems, and divisibility checks.

## How It Works 🔍

1. **Function `get_factors(num)`**:

    - Returns a list of all factors of the given natural number `num`.
    - Factors are integers that divide `num` exactly without leaving a remainder.

2. **Function `number_of_factors(num)`**:

    - Calls the `get_factors` function to get all factors of `num`.
    - Returns the number of factors by calculating the length of the list returned by `get_factors`.

3. **Example**:
   For the input `num = 12`, the factors will be `[1, 2, 3, 4, 6, 12]`, and the program will output the count `6`.

## Output 📜

For the input:

```
num = 12
```

The program will output:

```
6
```

## Usage 📦

1. Copy the code into a Python file, e.g., `number_of_factors.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python number_of_factors.py
    ```
5. Input a natural number, and the program will print the number of factors of that number.

## Conclusion 🚀

This program efficiently calculates the number of factors of a given number, making it useful for mathematical analysis and number-related tasks.

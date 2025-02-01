# Math Function Application Program

## Description

This program takes a number and a function name from the user and applies the corresponding mathematical function to the given number. It supports several functions, such as square, cube, square root, modulus, and sine. The function is applied to the number, and the result is displayed.

## Purpose

The program provides a way to dynamically apply mathematical operations to a number based on user input. The user can choose from predefined mathematical functions and get the corresponding result.

## How It Works

1. The program defines functions for square, cube, square root, modulus, and sine operations.
2. It uses a dictionary `my_actions` to map function names (in Russian) to the corresponding function.
3. The user is prompted to enter a number and a function name.
4. The `do_action()` function applies the chosen function to the number and prints the result.

## Usage

```python
number = int(input("Enter a number: "))
action = input("Enter the function name (square, cube, sqrt, modulus, sin): ").strip().lower()

do_action(my_actions, number)
```

For example:

-   If the user enters `4` and `квадрат`, the result will be `16` (square of 4).
-   If the user enters `27` and `куб`, the result will be `19683` (cube of 27).
-   If the user enters `9` and `корень`, the result will be `3.0` (square root of 9).
-   If the user enters `-5` and `модуль`, the result will be `5.0` (modulus of -5).
-   If the user enters `0.5` and `синус`, the result will be `0.479425538604203` (sine of 0.5 radians).

## Output

Example:

```
Enter a number: 4
Enter the function name (square, cube, sqrt, modulus, sin): квадрат
16
```

## Conclusion

This program allows users to dynamically perform mathematical operations on a number by simply specifying the operation they want. It is flexible and easy to use, with support for basic mathematical functions.

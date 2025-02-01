# Data Processing Program

## Description

This program processes three lists of data: a list of floating-point numbers, a list of words, and a list of integers.
The program performs the following operations:

1. Converts a list of floats into a list of squared and rounded values to one decimal place.
2. Filters the list of words to leave only palindromes longer than 4 characters.
3. Finds the product of the numbers in the given list of integers.

The program aims to perform these tasks efficiently and correctly, applying mapping, filtering, and reducing operations.

## Purpose

The goal of this program is to transform and filter the provided lists in specific ways:

-   **Squares and rounding**: The floating-point numbers are squared and rounded to one decimal place.
-   **Palindromes**: The list of words is filtered to leave only those that are palindromes longer than 4 characters.
-   **Product of numbers**: The program calculates the product of all integers in the list.

## How It Works

1. **Squaring and rounding**: The program uses a mapping operation to square each float and round the result to one decimal place.
2. **Filtering palindromes**: The program filters the words, leaving only those that are palindromes and have more than 4 characters.
3. **Product of numbers**: The program calculates the product of all integers in the list using a reducing operation.

## Output

The program outputs the following:

-   A list of squared and rounded float values.
-   A list of palindromes longer than 4 characters.
-   The product of all integers in the numbers list.

### Example Output:

```
[18.9, 37.1, 10.6, 95.4, 4.7, 78.9, 21.0, 1175.7, 146.9, 21.8, 6.0, 87.0]
['racecar', 'TATTARRATTAT', 'malayalam']
12360
```

## Usage

To use the program, call the `process_data` function with the appropriate input lists:

1. **floats**: A list of floating-point numbers.
2. **words**: A list of words.
3. **numbers**: A list of integers.

The function will return a tuple containing:

-   A list of squared and rounded floats.
-   A list of palindromes longer than 4 characters.
-   The product of the numbers in the list.

## Conclusion

This program successfully processes the input lists by performing squaring and rounding, filtering palindromes, and calculating the product of numbers.
The code uses functional programming concepts such as `map()`, `filter()`, and `reduce()` to achieve the desired result in an efficient and clean manner.

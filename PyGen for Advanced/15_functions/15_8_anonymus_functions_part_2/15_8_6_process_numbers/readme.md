# Filtering and Transforming Numbers

## Description

This program processes a list of numbers using Python's built-in functions `filter()` and `map()`. The steps involved are:

1. **Filtering**: Remove all odd numbers greater than 47.
2. **Transformation**: Divide all even numbers by 2 using integer division (`//`).

## Purpose

The objective is to practice functional programming by using `filter()` for selection criteria and `map()` for transformation.

## How It Works

1. **Filtering Condition**:

    - Retain numbers that are **≤ 47**.
    - If a number is **> 47**, keep it only if it is even.

2. **Transformation Rule**:

    - If a number is **even**, divide it by `2` (integer division).
    - Odd numbers remain unchanged.

3. **Processing**:
    - `filter()` is used with a lambda function to apply the filtering condition.
    - `map()` is used to apply the transformation rule.

## Output

The transformed numbers are printed on a single line, space-separated.

## Usage

1. **Define `input_numbers`**, the list of integers to process.
2. **Apply `filter()`** to remove odd numbers greater than 47.
3. **Apply `map()`** to divide even numbers by `2`.
4. **Print the result** as a space-separated string.

## Conclusion

This solution effectively demonstrates how to use Python's functional programming tools (`filter()` and `map()`) for data processing.

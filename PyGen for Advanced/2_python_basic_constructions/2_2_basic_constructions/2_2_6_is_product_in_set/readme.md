# Product of Two Numbers in a Set Program 🔢

## Description 📝

This program checks whether a given number can be expressed as the product of two distinct numbers from a set.
The set of numbers is provided as input, and the program outputs “YES” if such a pair exists, otherwise it outputs “NO”.

## Purpose 🎯

The program is designed to determine whether a target number is the product of two distinct numbers from a provided set of integers.
The number cannot be the product of the same element twice, meaning the indices of the two numbers must differ.

## How It Works 🔍

1. **Input Format**:

    - The first line contains the number `n`, which represents the number of integers in the set.
    - The next `n` lines contain the integers of the set (which may be repeated).
    - The last input is the target number that we need to check if it can be expressed as the product of two distinct numbers from the set.

2. **Logic**:

    - The program checks every pair of distinct numbers in the set to see if their product equals the target.
    - If such a pair is found, the program outputs “YES”. If no such pair is found after checking all combinations, it outputs “NO”.

3. **Example**:

    - **Input**:
        ```
        5
        2
        3
        4
        6
        8
        12
        ```
    - **Output**:
        ```
        YES
        ```
    - **Explanation**:
        - The product `2 * 6 = 12`, so the result is "YES".

4. **Edge Cases**:
    - If the set has fewer than two elements, the program will return “NO” since there are no pairs to multiply.
    - If the target cannot be expressed as the product of any two distinct elements, the program will output “NO”.

## Usage 📦

1. Copy the code into a Python file, e.g., `product_in_set.py`.
2. Run the script in the terminal:
    ```bash
    python product_in_set.py
    ```
3. Enter the number of elements in the set, followed by the elements themselves.
4. Enter the target number.
5. The program will output “YES” or “NO” based on whether the target can be expressed as the product of two distinct numbers from the set.

## Conclusion 🚀

This program efficiently determines whether a number can be expressed as the product of two distinct numbers from a given set.
It handles repeated elements and ensures that the two factors are distinct by checking their indices.
The program is simple yet effective for this task.

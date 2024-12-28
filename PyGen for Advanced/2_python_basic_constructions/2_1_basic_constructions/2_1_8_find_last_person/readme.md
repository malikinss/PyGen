# Josephus Problem Program 🔄

## Description 📝

This program solves the Josephus problem, where `n` people stand in a circle, and every `k`-th person is eliminated in each round until only one person remains.
The program calculates the position of the last remaining person in the circle.

## Purpose 🎯

The purpose of the program is to determine the position of the last person remaining after repeatedly eliminating every `k`-th person from a group of `n` people standing in a circle.

## How It Works 🔍

1. **Input Format**:
    - The program first reads two integer inputs: `n` (the total number of people) and `k` (the step size, or the position of the person to be eliminated in each round).
2. **Logic**:

    - The program implements an iterative solution to the Josephus problem using a mathematical formula:
        - Starting from the first person (0-indexed), the position of the last remaining person is calculated by updating the survivor's position with each iteration. The formula used is:
            ```python
            res = (res + k) % i
            ```
        - The final result is adjusted to be 1-indexed by adding 1.

3. **Example**:

    - **Input**:
        ```
        5
        2
        ```
    - **Output**:
        ```
        3
        ```
    - **Explanation**: With 5 people and eliminating every 2nd person, the survivor will be in position 3.

4. **Edge Cases**:
    - If `n = 1`, the survivor will always be the first person (position 1).
    - The program works efficiently even with large values of `n` and `k`.

## Usage 📦

1. Copy the code into a Python file, e.g., `josephus_problem.py`.
2. Run the script in the terminal:
    ```bash
    python josephus_problem.py
    ```
3. Enter the total number of people and the step size (the `k`-th person to be eliminated):

    - First, the number of people `n`.
    - Then, the step size `k`.

4. The program will output the position of the last person remaining in the circle.

## Conclusion 🚀

This program efficiently calculates the position of the last person remaining in the circle using a well-known mathematical solution to the Josephus problem. It can be used for any size circle and step size, offering a quick and reliable solution for such problems.

# Infinite Random Number Generator

## Description 📝

This Python script defines the `random_numbers()` function, which creates an infinite iterator that generates random integers within a given range.
The range is defined by two arguments: `left` (inclusive) and `right` (inclusive).

## Purpose 🎯

The purpose of this function is to generate an infinite sequence of random integers.
This is useful when you need an endless stream of random values within a specific range for simulations, testing, or other purposes.

## How It Works 🔍

1. **Input**: The function takes two arguments:
    - `left`: The lower bound of the range (inclusive).
    - `right`: The upper bound of the range (inclusive).
2. **Random Integer Generation**: The function uses `random.randint()` to generate random integers within the specified range.
3. **Infinite Sequence**: It returns an iterator that continuously generates random integers by using `iter()` and a lambda function, which calls `random.randint()` on each iteration.

## Output 📜

The function returns an iterator that produces random integers in the range `[left, right]` indefinitely.

## Usage 📦

1. Save the code to a file named `random_number_generator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```python
    python random_number_generator.py
    ```
5. Call the function `random_numbers()` to create an iterator and generate random numbers. Example:
    ```python
    rand_gen = random_numbers(1, 100)
    print(next(rand_gen))  # Prints a random number between 1 and 100
    ```

## Conclusion 🚀

This function provides an efficient way to generate an infinite stream of random numbers within a specified range.
It’s ideal for tasks that require a constant flow of random data, such as simulations and testing environments.

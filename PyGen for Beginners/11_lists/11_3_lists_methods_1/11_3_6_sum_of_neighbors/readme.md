# Sum of Neighboring Numbers 📝

## Description 📝

This Python program takes a natural number `n` (where `n ≥ 2`) and a list of `n` integers as input. It generates a new list where each element is the sum of two consecutive numbers from the input list.

## Purpose 🎯

The program demonstrates how to generate a list of sums from neighboring elements in a given list of integers.

## How It Works 🔍

1. The function `sum_of_neighbors()` takes two parameters: `n` (the number of integers) and `numbers` (the list of integers).
2. The function uses list comprehension to compute the sum of each pair of neighboring integers: `numbers[i] + numbers[i+1]`.
3. The result is returned as a list of sums.

## Output 📜

```bash
Example Input:
5
1
2
3
4
5
Example Output:
[3, 5, 7, 9]
```

## Usage 📦

1. Save the script as `sum_of_neighbors.py`.
2. Run the script in a Python environment.
3. Input the number n (where n ≥ 2).
4. Input n integers.
5. The program will output a list of sums of neighboring numbers.

## Conclusion 🚀

This program efficiently calculates the sums of neighboring numbers in a list using list comprehension, demonstrating basic Python programming skills.

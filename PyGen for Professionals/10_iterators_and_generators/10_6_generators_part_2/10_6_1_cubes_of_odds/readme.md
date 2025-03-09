# Cubes of Odd Numbers Generator

## Description 📝

This Python script defines the `cubes_of_odds()` function, which takes an iterable of integers and returns a generator that yields the cubes of all odd numbers in the input sequence.
The implementation uses a generator expression for efficiency and readability.

## Purpose 🎯

The goal of this function is to efficiently generate cubes of odd numbers from a given iterable.
Instead of storing the entire result in memory, it yields values one by one, making it memory-efficient.

## How It Works 🔍

1. **Generator Expression**: The function returns a generator expression that iterates over the input iterable.
2. **Filtering Odd Numbers**: It checks if each number is odd (`number % 2` evaluates to `True` for odd numbers).
3. **Cubing the Odd Numbers**: If the number is odd, it is raised to the third power (`number ** 3`) and yielded.

## Output 📜

Example usage:

```python
nums = [1, 2, 3, 4, 5]
for num in cubes_of_odds(nums):
    print(num)
```

Output:

```
1
27
125
```

## Usage 📦

1. Save the code to a file named `cubes_of_odds.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script in a Python environment:
    ```python
    nums = [1, 2, 3, 4, 5]
    print(list(cubes_of_odds(nums)))
    ```
5. The function can be used in loops, list comprehensions, or with `list()` to generate all values at once.

## Conclusion 🚀

This function is a concise and memory-efficient way to compute cubes of odd numbers from a given iterable.
By leveraging a generator expression, it avoids unnecessary memory consumption while maintaining readability and efficiency.

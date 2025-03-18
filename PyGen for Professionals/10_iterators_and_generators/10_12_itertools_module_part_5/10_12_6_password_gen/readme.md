# Three-Character Password Generator

## Description 📝

The `password_gen()` function generates all possible three-character passwords using the digits from 0 through 9.
It uses the `product()` function from the `itertools` module to generate all combinations of the digits with a length of 3 in ascending order.

## Purpose 🎯

This function allows for generating all possible three-character passwords in a structured and efficient manner, which can be useful for tasks involving password validation or brute force simulations.

## How It Works 🔍

-   **Using `product()`**: The `product()` function from `itertools` generates all possible combinations of the provided iterable (`range(10)`), repeated 3 times (for each character in the password).
    -   The `map(str, range(10))` converts digits 0-9 into strings.
    -   The `repeat=3` ensures that the combinations will be of length 3.
-   **Generator**: The function yields each combination as a string by joining the elements of the combination tuple.

## Output 📜

Example usage:

```python
for password in password_gen():
    print(password)
# Output: 000, 001, 002, 003, ..., 999
```

## Usage 📦

1. Save the function in a Python file, e.g., `password_gen.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the function:
    ```python
    from password_gen import password_gen
    for password in password_gen():
        print(password)  # Output: 000, 001, 002, ..., 999
    ```

## Conclusion 🚀

The `password_gen()` function provides a simple yet effective way to generate all possible three-character passwords composed of digits from 0 through 9.
Using `product()` helps efficiently generate the combinations, making the code both readable and performant.

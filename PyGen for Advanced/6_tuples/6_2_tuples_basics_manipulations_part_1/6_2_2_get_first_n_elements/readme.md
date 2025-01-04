# Get the First N Elements from a Tuple 🔢

## Description 📝

This program demonstrates how to extract the first `n` elements from a tuple using slicing. The function `get_first_n_elements` returns a tuple containing the first `n` elements from the given tuple.

## Purpose 🎯

-   To extract the first `n` elements from a tuple using Python's slicing technique.
-   Showcase the usage of the slice operator (`[:]`) to retrieve a specific range of elements from a tuple.

## How It Works 🔍

1. **Function `get_first_n_elements(tup: Tuple[int, ...], n: int)`**:

    - Takes a tuple `tup` and an integer `n` as arguments.
    - Uses slicing (`tup[:n]`) to get the first `n` elements from the tuple.
    - Returns the sliced tuple containing the first `n` elements.

2. **Tuple `primes`**:
    - Contains a sequence of prime numbers.
3. **The result**:
    - The function is called to retrieve the first 6 elements of the `primes` tuple, which is then printed.

### Example:

```
Input: Tuple of prime numbers, n = 6
Output: The first 6 prime numbers
```

## Output 📜

The output will be:

```
(2, 3, 5, 7, 11, 13)
```

## Conclusion 🚀

This code effectively demonstrates the use of slicing to access the first `n` elements of a tuple, providing a clean and simple way to retrieve a subset of the tuple.

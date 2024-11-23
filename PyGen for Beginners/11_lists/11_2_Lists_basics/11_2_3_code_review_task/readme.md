# Code Review Task 18 🪲

## Description 📝

This task extends the previous Python script to output the first 6 elements of the `primes` list using slicing. It demonstrates how to use list slicing to extract a portion of a list.

## Purpose 🎯

The purpose of this program is to:

1. Demonstrate how to extract a portion of a list using slicing.
2. Show how to retrieve the first `n` elements from a list.

## How It Works 🔍

-   The program defines a list of prime numbers.
-   It uses slicing `[:6]` to access the first 6 elements of the list.
-   The first 6 elements are then printed to the console.

## Output 📜

-   The program prints the first 6 prime numbers in the list:  
    `2, 3, 5, 7, 11, 13`

## Identified Errors in the Original Code 🕵🏾:

1. **Using slicing to get the first 6 elements**:
    - Original: The code needed to extract the first 6 elements from the list.
    - Fix: Used slicing `[:6]` to access the first 6 elements of the list.

## Fixed Code 🛠:

```python
# List of prime numbers
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# Print the first 6 elements of the list
print(primes[:6])
# Outputs: [2, 3, 5, 7, 11, 13]
```

## Explanation of Changes 🧾:

1. **Using slicing**: The code uses `primes[:6]` to extract the first 6 elements from the list.
2. **Output**: The first 6 prime numbers are printed as `[2, 3, 5, 7, 11, 13]`.

## Conclusion 🚀

This task demonstrates how to use list slicing to extract a subset of elements from a list, in this case, the first 6 elements.

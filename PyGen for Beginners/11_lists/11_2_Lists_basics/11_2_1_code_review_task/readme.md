# Code Review Task 16 🪲

## Description 📝

This task updates a Python script to print the 17th element of a list, considering the 1-based index, of a list of prime numbers.

## Purpose 🎯

The purpose of this program is to:

1. Demonstrate how to access list elements using an index in Python.
2. Show how to handle 0-based indexing when needing a specific 1-based index.
3. Output the prime number located at the 17th position (1-based) in the list.

## How It Works 🔍

-   The program defines a list of prime numbers.
-   It uses the indexer to access the 17th element in the list, which corresponds to the element at index 16 (since Python uses 0-based indexing).
-   The element is printed to the console.

## Output 📜

-   The program prints the 17th prime number:  
    `59`

## Identified Errors in the Original Code 🕵🏾:

1. **Accessing the 17th element**:
    - Original: No issue with the logic, but the code needed to correctly reference the element using Python's 0-based indexing.
    - Fix: Used index `16` to correctly access the 17th element (since the first element is at index `0`).

## Fixed Code 🛠:

```python
# List of prime numbers
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# Print the 17th element (1-based index)
print(primes[16])
# Outputs: 59
```

## Explanation of Changes 🧾:

1. `Using indexer`: Accessed the 17th element using `primes[16]`, as Python uses 0-based indexing. This correctly prints the 17th prime number.
2. `Output`: The prime number `59` is printed, which is at the 17th position in the list.

## Conclusion 🚀

This task demonstrates list indexing in Python, highlighting the conversion from a 1-based index to a 0-based index for correct element retrieval.

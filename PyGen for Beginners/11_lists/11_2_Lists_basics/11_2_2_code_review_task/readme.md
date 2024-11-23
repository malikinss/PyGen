# Code Review Task 🪲

## Description 📝

This task updates a Python script to print the last element of the `primes` list using an indexer.
It demonstrates how to access the last item in a list.

## Purpose 🎯

The purpose of this program is to:

1. Show how to access the last element of a list using negative indexing in Python.
2. Demonstrate Python's ability to use `-1` to refer to the last item in a list.

## How It Works 🔍

-   The program defines a list of prime numbers.
-   It uses the indexer `-1` to access the last element in the list, which is the prime number `71` in this case.
-   The last element is printed to the console.

## Output 📜

-   The program prints the last prime number in the list:  
    `71`

## Identified Errors in the Original Code 🕵🏾:

1. **Accessing the last element**:
    - Original: The code needed to access the last element using an appropriate index.
    - Fix: Used negative indexing `-1` to directly access the last element of the list.

## Fixed Code 🛠:

```python
# List of prime numbers
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# Print the last element of the list
print(primes[-1])
# Outputs: 71
```

## Explanation of Changes 🧾:

1. **Using negative indexing**: The code uses `primes[-1]` to correctly access the last element in the list.
2. **Output**: The prime number `71` is printed, which is the last element in the list.

## Conclusion 🚀

This task demonstrates how to efficiently access the last element of a list using Python's negative indexing, making the code cleaner and more intuitive.

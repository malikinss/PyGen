# Tribonacci Sequence Generator Program 📈

## Description 📝

This program generates the first `n` numbers of the Tribonacci sequence.
The Tribonacci sequence starts with three 1's: 1, 1, 1, and each subsequent number is the sum of the previous three numbers.

## Purpose 🎯

-   To demonstrate how to generate a sequence based on a recursive relationship.
-   To practice handling sequences and loops in Python.

## How It Works 🔍

1. **Function `generate_tribonacci(n)`**:

    - Initializes the first three numbers of the Tribonacci sequence: `1, 1, 1`.
    - For each subsequent number, it computes the sum of the last three numbers.
    - Adds each generated number to the result list.

2. **Main Program**:
    - Reads the input `n`, the number of terms in the Tribonacci sequence to generate.
    - Calls the `generate_tribonacci(n)` function to compute the sequence and then prints the result.

### Example:

```

Input:
5

Output:
1 1 1 3 5

```

## Output 📜

For `n = 5`, the program will output:

```

1 1 1 3 5

```

## Conclusion 🚀

This program successfully generates and prints the first `n` numbers of the Tribonacci sequence based on the input provided.
It highlights the use of loops and basic sequence generation in Python.

# Number Printer with Exclusions

## Description 📝

This program prints numbers from \( 1 \) to \( n \) inclusive, while excluding numbers in the following ranges:

-   \( 5 \) to \( 9 \) inclusive,
-   \( 17 \) to \( 37 \) inclusive,
-   \( 78 \) to \( 87 \) inclusive.

The program ensures that these ranges are skipped efficiently without disrupting the sequence of output numbers.

## Purpose 🎯

To demonstrate conditional filtering within loops in Python and showcase handling of specific number ranges using control flow structures.

## How It Works 🔍

1. The program accepts a natural number \( n \) as input.
2. It iterates through numbers from \( 1 \) to \( n \).
3. For each number:
    - If the number falls into any of the exclusion ranges:
        - \( 5 \leq x \leq 9 \),
        - \( 17 \leq x \leq 37 \),
        - \( 78 \leq x \leq 87 \),
          it skips printing that number.
    - Otherwise, the number is printed.
4. The loop continues until all numbers from \( 1 \) to \( n \) are processed.

### Example

```bash
Input:
20

Output:
1 2 3 4 10 11 12 13 14 15 16

```

## Output 📜

The program outputs all numbers from \( 1 \) to \( n \), excluding the specified ranges.

## Usage 📦

1. Run the script in a Python environment.
2. Input a natural number \( n \) when prompted.
3. Observe the printed sequence with excluded ranges.

### Example Usage

1. Run the script.
2. Input: `n = 20`.
3. Output: `1, 2, 3, 4, 10, 11, ...`.

## Conclusion 🚀

This program provides a straightforward example of handling conditions and exclusions in loops.
It is useful for scenarios requiring selective number processing based on specific ranges.

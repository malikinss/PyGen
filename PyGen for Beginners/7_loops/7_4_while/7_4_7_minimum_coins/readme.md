# Minimum Coins to Pay the Witcher

## Description 📝

This program determines the minimum number of minted coins needed to reach a specific amount.
The denominations available in the world of the Witcher are 1, 5, 10, and 25.
The program calculates how many coins of these denominations are needed to form a given amount, ensuring the fewest number of coins are used.

## Purpose 🎯

The program demonstrates how to solve the classic "coin change problem" with a greedy algorithm.
It minimizes the number of coins needed to reach a given amount by always choosing the largest coin denomination available.

## How It Works 🔍

1. The program accepts an integer `n`, which represents the amount to be paid.
2. It iterates through the available coin denominations (25, 10, 5, and 1) starting with the largest denomination.
3. For each denomination, the program subtracts the coin value from `n` as many times as possible, incrementing the coin counter.
4. The result is the total number of coins used to form the amount.

### Example

```bash
Input: 68
Output: Minimum coins required: 6

```

In this example:

-   2 coins of denomination 25 (50)
-   1 coin of denomination 10 (10)
-   1 coin of denomination 5 (5)
-   3 coins of denomination 1 (3)

## Output 📜

The output is the minimum number of coins needed to make the given amount using the available denominations.

## Usage 📦

1. Run the script in a Python environment.
2. Enter the amount to be paid.
3. The program will output the minimum number of coins required to make the amount.

## Conclusion 🚀

This program efficiently solves the coin change problem by using a greedy approach, which is optimal when the coin denominations are multiples of each other.

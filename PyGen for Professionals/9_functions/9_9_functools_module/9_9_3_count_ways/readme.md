# Ways to Climb Stairs 📝

## Description 📝

Dima wants to climb a staircase, but he can only climb 1, 3, or 4 steps at a time (not 2 steps).
This program calculates the number of distinct ways to reach the n-th step given that restriction.

## Purpose 🎯

The purpose of this function is to calculate how many ways Dima can climb to the n-th step, considering that he can only take 1, 3, or 4 steps at a time.

## How It Works 🔍

1. The function takes a natural number `n` as input, which represents the number of the step Dima needs to reach.
2. It uses dynamic programming (with memoization) to calculate the number of ways to reach the n-th step by recursively considering the possibilities of taking 1, 3, or 4 steps at each stage.
3. The program uses memoization to store intermediate results and speed up repeated calculations.

## Output 📜

The program returns the number of distinct ways to reach the n-th step, with the restriction of climbing 1, 3, or 4 steps at a time.

Example:

```
Input:
5
Output:
4

Explanation:
The four possible ways to reach the 5th step are:
1→2→3→4→5
1→4→5
1→2→5
1→5
```

## Usage 📦

1. Call the `count_ways(n)` function with a positive integer `n` (where `n ≤ 100`).
2. The function will return the number of ways to reach the n-th step, considering the allowed step sizes.

## Conclusion 🚀

This program provides an efficient way to calculate the number of distinct ways to climb the stairs with given step restrictions.
By using dynamic programming and memoization, it handles even the largest values of `n` efficiently.

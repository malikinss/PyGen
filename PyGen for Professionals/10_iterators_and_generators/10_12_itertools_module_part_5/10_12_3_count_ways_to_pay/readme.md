# `count_ways_to_pay()`: Count Unique Ways to Pay a Target Amount

## Description 📝

The function `count_ways_to_pay()` calculates the number of **distinct ways** to pay a specific target amount using the given bill denominations, where each denomination can be used multiple times.
The key point is that the order of the bills doesn't matter, so combinations like `[50, 20, 20]` and `[20, 50, 20]` are counted as the same.

## Purpose 🎯

This function is useful for:  
✔️ **Calculating the number of distinct ways** to achieve a specific target sum using multiple available denominations.  
✔️ **Considering combinations without the importance of order**, so `[20, 50]` and `[50, 20]` would count as one.

## How It Works 🔍

1. **Combinations with Replacement**: The function generates combinations of the bill denominations with the `combinations_with_replacement` method from `itertools`, which allows repeated use of a denomination.
2. **Sum Matching**: For each combination, the function checks whether the sum equals the target amount.
3. **Set for Uniqueness**: It uses a set to store sorted combinations to ensure uniqueness (duplicates in different orders are discarded).
4. **Counting**: It returns the number of distinct combinations that sum to the target amount.

## Output 📜

### Example 1: Number of Ways to Pay $100

```python
>>> wallet = [100, 50, 20, 10, 5]
>>> target_amount = 100
>>> count_ways_to_pay(wallet, target_amount)
50
```

**Explanation**:

-   There are **50 distinct ways** to pay $100 using the available denominations.
    These include combinations of various bills like $100, $50, $20, $10, and $5, where the order doesn't matter.

### Example 2: Number of Ways to Pay with a Single Denomination

```python
>>> wallet = [20]
>>> target_amount = 100
>>> count_ways_to_pay(wallet, target_amount)
1
```

**Explanation**:

-   There is only **1 way** to pay $100 using $20 bills: `[20, 20, 20, 20, 20]`.

## Conclusion 🚀

The `count_ways_to_pay()` function is now correctly counting the **50 unique ways** to pay the target amount of $100 with the available denominations.
It handles all combinations, ensuring duplicates are not counted by using sorted tuples and a set.
This approach is particularly useful for solving combinatorial problems with repetition, where the order doesn't matter.

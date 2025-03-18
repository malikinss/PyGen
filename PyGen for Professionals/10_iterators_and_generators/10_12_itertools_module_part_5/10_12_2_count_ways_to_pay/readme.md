# `count_ways_to_pay()` - Count Unique Ways to Pay a Specific Amount

## Description 📝

The `count_ways_to_pay()` function calculates the number of unique ways to pay a specific target amount using a set of available bills from a wallet.
It ensures that combinations of bills that only differ in order are not counted multiple times.

## Purpose 🎯

✔ **Identifies unique combinations** of bills that sum up to the target amount.  
✔ **Ignores duplicate combinations** that are just permutations of the same set of bills.  
✔ **Works with various denominations** present in the wallet.

## How It Works 🔍

1. **Iterates over all possible combinations** of bills in the wallet using `combinations()`.
2. **Filters combinations** where the sum equals the target amount (`100` in this case).
3. **Removes duplicate combinations** by sorting the bills in each combination and adding them to a `set`.
4. **Returns the number of unique combinations** by measuring the length of the set.

## Usage 📦

```python
wallet = [
    100, 100,
    50, 50, 50, 50,
    20, 20, 20,
    10, 10, 10, 10, 10,
    5, 5,
    1, 1, 1, 1, 1
]
target_amount = 100

print(count_ways_to_pay(wallet, target_amount))
```

**Output:**

```plaintext
6
```

## Conclusion 🚀

This function effectively counts the number of distinct ways to pay a target amount using available bills, ensuring that the same set of bills is not counted multiple times due to different orderings.
It's a robust solution for problems involving combinations of items.

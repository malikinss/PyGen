# `ranges()` - Convert Numbers into Segments

## Description 📝

The `ranges()` function takes a sorted list of distinct natural numbers and transforms consecutive numbers into segments.
Each segment is represented as a tuple, where the first element is the left border and the second is the right border.

## Purpose 🎯

✔ **Groups consecutive numbers** into segments.  
✔ **Preserves the original order** of numbers in the input list.  
✔ **Handles single numbers correctly** by treating them as segments with identical borders.

## How It Works 🔍

1. **Uses `groupby()`** to group consecutive numbers.
2. **Defines a key function** that assigns numbers to groups based on their difference from an incrementing counter.
3. **Creates segment tuples** where the first element is the start of a group and the second is the end.
4. **Returns a list of these tuples** representing the number segments.

## Usage 📦

```python
numbers_list = [1, 2, 3, 4, 7, 8, 10]

result = ranges(numbers_list)
print(result)
```

**Output:**

```plaintext
[(1, 4), (7, 8), (10, 10)]
```

## Conclusion 🚀

This function efficiently groups consecutive numbers into segments while maintaining order.
It works well for various cases, including single numbers and multiple disjoint sequences.

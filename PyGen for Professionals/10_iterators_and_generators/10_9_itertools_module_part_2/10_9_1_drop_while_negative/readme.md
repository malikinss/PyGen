# `drop_while_negative()`: Skipping Negative Numbers

## Description 📝

The `drop_while_negative()` function processes an iterable of integers and returns an iterator that **skips all negative numbers**, starting from the **first non-negative number** (zero or positive).

## Purpose 🎯

This function is useful when you need to ignore initial negative values and begin processing from the first non-negative integer while preserving the original order.

## How It Works 🔍

1. **Uses `dropwhile()` from `itertools`**

    - Skips all elements while the condition (`x < 0`) is **True**.
    - As soon as the condition becomes **False** (i.e., the first non-negative number is encountered), it stops skipping.

2. **Preserves order**
    - All remaining elements (including zero and positive numbers) are **yielded** as they appear in the original iterable.

## Output 📜

An **iterator** that yields elements from the first non-negative number onward.

### Example 1: Normal Case

```python
>>> list(drop_while_negative([-3, -2, -1, 0, 1, 2]))
[0, 1, 2]
```

**Explanation**:

-   `-3, -2, -1` are skipped because they are negative.
-   `0, 1, 2` are yielded because the first non-negative (`0`) is encountered.

### Example 2: All Negative Numbers

```python
>>> list(drop_while_negative([-5, -4, -3]))
[]
```

**Explanation**:

-   Since **no non-negative numbers exist**, the function returns an **empty iterator**.

### Example 3: No Negative Numbers

```python
>>> list(drop_while_negative([1, 2, 3]))
[1, 2, 3]
```

**Explanation**:

-   Since the iterable starts with a non-negative number, it **remains unchanged**.

## Usage 📦

1. Call `drop_while_negative(iterable)`, passing an iterable of integers.
2. The function will return an iterator that can be used in a loop or converted to a list.

```python
iter_numbers = drop_while_negative([-10, -5, 0, 2, 4])
for num in iter_numbers:
    print(num)
# Output: 0, 2, 4
```

## Conclusion 🚀

The `drop_while_negative()` function efficiently skips negative values using **lazy evaluation**, making it memory-efficient for large sequences. ⚡

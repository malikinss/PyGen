# `max_pair()`: Find the Maximum Sum of Two Adjacent Numbers

## Description 📝

The `max_pair()` function calculates the **maximum sum** of any two **adjacent numbers** in the given iterable.  
It works by evaluating the sums of each pair of consecutive elements and returning the largest sum.

## Purpose 🎯

This function is useful for:  
✔️ **Identifying the most significant pairwise sum** in a sequence.  
✔️ **Finding the highest adjacent relationship** between numbers.  
✔️ **Analyzing sequences** where the sum of adjacent numbers matters.

## How It Works 🔍

1. The function uses `pairwise()` from `itertools` to generate pairs of adjacent numbers.
2. It then uses `starmap()` to apply the sum operation to each pair.
3. Finally, `max()` is used to find the maximum sum of all the pairs.

---

## Output 📜

### Example 1: Maximum Pair Sum

```python
>>> max_pair([1, 8, 2, 4, 3])
10
```

**Explanation**:

-   The adjacent pairs are: `(1, 8)`, `(8, 2)`, `(2, 4)`, and `(4, 3)`.
-   The sums of these pairs are `9`, `10`, `6`, and `7`.
-   The maximum sum is `10`.

---

### Example 2: Negative and Positive Numbers

```python
>>> max_pair([-1, -5, 3, 2, 6])
8
```

**Explanation**:

-   The adjacent pairs are: `(-1, -5)`, `(-5, 3)`, `(3, 2)`, and `(2, 6)`.
-   The sums are `-6`, `-2`, `5`, and `8`.
-   The maximum sum is `8`.

---

### Example 3: All Elements are Equal

```python
>>> max_pair([5, 5, 5, 5])
10
```

**Explanation**:

-   The adjacent pairs are: `(5, 5)`, `(5, 5)`, `(5, 5)`.
-   The sums are `10`, `10`, and `10`.
-   The maximum sum is `10`.

---

### Example 4: Sequence with Larger Numbers

```python
>>> max_pair([1000, 2000, 3000, 4000])
7000
```

**Explanation**:

-   The adjacent pairs are: `(1000, 2000)`, `(2000, 3000)`, `(3000, 4000)`.
-   The sums are `3000`, `5000`, and `7000`.
-   The maximum sum is `7000`.

---

## Usage 📦

Use `max_pair()` when you need to find the largest sum of adjacent elements in an iterable.

```python
numbers = [1, 5, 10, 2, 3]
result = max_pair(numbers)
print(result)  # Output: 15
```

---

## Conclusion 🚀

The `max_pair()` function is a quick and efficient way to **find the highest sum** of adjacent numbers in a sequence.  
It works well for various types of iterables, including lists, tuples, and generators, and ensures a **precise comparison** of adjacent relationships.

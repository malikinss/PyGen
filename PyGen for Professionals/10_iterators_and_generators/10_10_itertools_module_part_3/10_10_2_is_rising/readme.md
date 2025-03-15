# `is_rising()`: Check if Elements are Strictly in Ascending Order

## Description 📝

The `is_rising()` function checks if the elements in the given iterable are in **strictly ascending order**.  
It returns `True` if each element is strictly greater than the one before it, and `False` otherwise.

## Purpose 🎯

This function is useful for:  
✔️ **Validating order** in a sequence of numbers.  
✔️ **Detecting trends** in datasets where values should increase.  
✔️ Ensuring **strict monotonicity** in sequences.

## How It Works 🔍

1. The function uses the `pairwise()` function from `itertools` to create pairs of consecutive elements from the iterable.
2. It then checks if each pair satisfies the condition `a < b` (strictly ascending).
3. The `all()` function ensures that this condition holds for every consecutive pair in the iterable.

---

## Output 📜

### Example 1: Strictly Ascending Sequence

```python
>>> is_rising([1, 2, 3, 4])
True
```

**Explanation**:

-   The elements `1, 2, 3, 4` are in strictly ascending order, so the function returns `True`.

---

### Example 2: Non-strictly Ascending Sequence

```python
>>> is_rising([1, 2, 2, 4])
False
```

**Explanation**:

-   The second and third elements are the same (`2` and `2`), so the sequence is not strictly ascending. The function returns `False`.

---

### Example 3: Strictly Ascending Sequence with Negative Numbers

```python
>>> is_rising([-5, -4, -3, -2, -1])
True
```

**Explanation**:

-   The elements are strictly increasing in negative values, so the function returns `True`.

---

### Example 4: Single Decrease in the Sequence

```python
>>> is_rising([1, 2, 3, 2, 4])
False
```

**Explanation**:

-   The sequence decreases from `3` to `2`, so it is not strictly ascending. The function returns `False`.

---

## Usage 📦

Use `is_rising()` when you need to check if the elements in an iterable are in strictly increasing order.

```python
numbers = [1, 3, 5, 7]
result = is_rising(numbers)
print(result)  # Output: True
```

---

## Conclusion 🚀

The `is_rising()` function is a simple and efficient way to **check for strict monotonicity** in a sequence of numbers.  
It works well for sequences of various types, including lists and generators, and ensures a reliable way to validate that the elements are strictly increasing.

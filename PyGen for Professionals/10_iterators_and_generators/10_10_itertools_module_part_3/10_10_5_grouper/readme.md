# `grouper()`: Group Elements into Fixed-Size Tuples

## Description 📝

The `grouper()` function groups elements from an iterable into fixed-size `n`-element tuples.  
If the iterable does not have enough elements to complete the last group, `None` is used as a filler.

## Purpose 🎯

✔️ **Efficiently grouping elements** into fixed-size chunks.  
✔️ **Maintaining order** of elements while grouping.  
✔️ **Handling missing elements** gracefully by padding with `None`.  
✔️ **Creating batch processing mechanisms** for working with iterators.

## How It Works 🔍

1. `repeat(iter(iterable), n)`: Creates `n` independent iterators pointing to the same iterable.
2. `zip_longest()`: Collects one element from each iterator at a time, forming `n`-element tuples.
3. `fillvalue=None`: Ensures that missing values in the last tuple are replaced with `None`.

---

## Output 📜

### Example 1: Grouping into Pairs (`n=2`)

```python
>>> list(grouper([1, 2, 3, 4, 5], 2))
[(1, 2), (3, 4), (5, None)]
```

**Explanation**:

-   The elements are grouped into pairs: `(1,2)`, `(3,4)`, and `(5,None)`.
-   Since 5 has no adjacent element, it is padded with `None`.

---

### Example 2: Grouping into Triplets (`n=3`)

```python
>>> list(grouper([1, 2, 3, 4, 5], 3))
[(1, 2, 3), (4, 5, None)]
```

**Explanation**:

-   The first three elements form `(1,2,3)`, and the remaining elements form `(4,5,None)`.

---

### Example 3: Perfectly Divisible Iterable (`n=3`)

```python
>>> list(grouper([10, 20, 30, 40, 50, 60], 3))
[(10, 20, 30), (40, 50, 60)]
```

**Explanation**:

-   Since the length is exactly divisible by `3`, no `None` values are needed.

---

### Example 4: Single Element Groups (`n=1`)

```python
>>> list(grouper([7, 8, 9], 1))
[(7,), (8,), (9,)]
```

**Explanation**:

-   Each element forms a single-element tuple.

---

## Usage 📦

Use `grouper()` when you need to **batch process** elements while maintaining their order.

```python
numbers = [1, 2, 3, 4, 5]
grouped = list(grouper(numbers, 2))
print(grouped)  # Output: [(1, 2), (3, 4), (5, None)]
```

---

## Conclusion 🚀

The `grouper()` function is an **efficient and flexible** way to divide an iterable into equal-sized groups while ensuring that missing values are handled gracefully.  
It is particularly useful in **batch processing**, **data manipulation**, and **iterable transformations**.

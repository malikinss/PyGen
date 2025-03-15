# `ncycles()`: Generate a Sequence of Repeated Elements from an Iterable

## Description 📝

The `ncycles()` function creates an iterator that repeats the elements of the given iterable a specified number of times.  
The elements are returned in their original order, and the iterable is looped `times` times.

## Purpose 🎯

This function is useful for:  
✔️ **Repeating an iterable** multiple times without modifying the original order.  
✔️ **Creating circular sequences** for iterators in situations requiring repeated elements.  
✔️ **Efficiently iterating over elements** with controlled repetitions.

## How It Works 🔍

1. The function uses `tee()` from `itertools` to create multiple independent iterators from the same iterable.
2. `chain.from_iterable()` is used to concatenate the iterators into a single iterator that produces repeated elements.

---

## Output 📜

### Example 1: Repeat Iterable Twice

```python
>>> list(ncycles([1, 2, 3], 2))
[1, 2, 3, 1, 2, 3]
```

**Explanation**:

-   The iterable `[1, 2, 3]` is repeated twice, resulting in `[1, 2, 3, 1, 2, 3]`.

---

### Example 2: Repeat Iterable Three Times

```python
>>> list(ncycles([4, 5], 3))
[4, 5, 4, 5, 4, 5]
```

**Explanation**:

-   The iterable `[4, 5]` is repeated three times, resulting in `[4, 5, 4, 5, 4, 5]`.

---

### Example 3: Single Iteration

```python
>>> list(ncycles([7, 8], 1))
[7, 8]
```

**Explanation**:

-   The iterable `[7, 8]` is repeated once, returning the same sequence: `[7, 8]`.

---

### Example 4: Using with Larger Iterable

```python
>>> list(ncycles([10, 20, 30], 4))
[10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30]
```

**Explanation**:

-   The iterable `[10, 20, 30]` is repeated four times, resulting in `[10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30]`.

---

## Usage 📦

Use `ncycles()` when you need to create an **iterator** that produces elements of an iterable repeated a specified number of times.

```python
numbers = [1, 2, 3]
result = list(ncycles(numbers, 2))
print(result)  # Output: [1, 2, 3, 1, 2, 3]
```

---

## Conclusion 🚀

The `ncycles()` function is a flexible and efficient way to repeat the elements of an iterable multiple times while keeping the original order.  
This function works well with various iterable types and is especially useful when working with iterators in repetitive tasks or cyclic processes.

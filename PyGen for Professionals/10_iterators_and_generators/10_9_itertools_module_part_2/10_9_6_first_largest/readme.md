# `first_largest()`: Find Index of First Element Greater Than Given Number

## Description 📝

The `first_largest()` function returns the **index** of the first element in an iterable that is **greater** than a given number.  
If no such element is found, the function returns `-1`.

## Purpose 🎯

This function is useful for:  
✔️ **Finding the first number** that exceeds a specific value in a sequence.  
✔️ **Handling edge cases** where no element satisfies the condition.  
✔️ Efficiently **searching through an iterable** without needing to manually loop through it.

## How It Works 🔍

1. It uses `dropwhile()` from `itertools` to **skip all elements** until it finds one greater than the given number.
2. The function then retrieves the **index** of the first element that meets this condition.
3. If no such element is found, the function returns `-1`.

---

## Output 📜

### Example 1: Find the Index of First Element Greater Than Given Number

```python
>>> first_largest([10, 2, 14, 7, 7, 18, 20], 11)
2
```

**Explanation**:

-   The function finds that the **first number greater than 11** is `14`, located at index `2`.
-   The function returns `2`.

---

### Example 2: No Element Greater Than Given Number

```python
>>> first_largest([1, 2, 3], 5)
-1
```

**Explanation**:

-   Since no element in the list is greater than `5`, the function returns `-1`.

---

### Example 3: Accessing Index from a Generator

```python
>>> gen = (x * 2 for x in range(10))
>>> first_largest(gen, 10)
6
```

**Explanation**:

-   The function works with **generators** as well.
-   It finds that the **first element greater than 10** is `14`, which is at index `6`.

---

### Example 4: Empty Iterable

```python
>>> first_largest([], 1)
-1
```

**Explanation**:

-   The function returns `-1` if the iterable is empty and no element exists to meet the condition.

---

## Usage 📦

Use `first_largest()` when you need to **find the index** of the first element greater than a specified number in any iterable.

```python
numbers = [10, 20, 30, 40, 50]
result = first_largest(numbers, 25)
print(result)  # Output: 2
```

---

## Conclusion 🚀

The `first_largest()` function efficiently finds the **first element** in an iterable that exceeds a given threshold.  
It gracefully handles cases where no such element exists, returning `-1` in such scenarios.  
This simple and effective solution works with various iterable types, including lists, generators, and other sequences.

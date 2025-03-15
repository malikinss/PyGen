# `first_true()`: Finding the First Matching Element

## Description 📝

The `first_true()` function scans an iterable and **returns the first element** for which the given predicate function returns `True`.

-   If no element matches, it returns `None`.
-   If `predicate` is `None`, it defaults to the `bool()` function (treating truthy values as valid).

## Purpose 🎯

This function is useful for:  
✔️ Finding the **first occurrence** of a matching element.  
✔️ **Skipping falsy values** (`0, None, False, ""`, etc.).  
✔️ Providing a **custom condition** to filter elements.

## How It Works 🔍

1. If `predicate` is `None`, it defaults to `bool()`.
2. The function uses `filterfalse()` from `itertools` to **skip** elements where `predicate` returns `False`.
3. It retrieves the **first valid element** using `next()`.
4. If no matching element exists, `None` is returned.

---

## Output 📜

### Example 1: Find First Number Greater than 1

```python
>>> first_true([0, 0, 1, 2, 3], lambda x: x > 1)
2
```

**Explanation**:

-   Skips `0, 0, 1` since they **don't satisfy** `x > 1`.
-   Returns `2` (first number **greater than 1**).

---

### Example 2: Finding First Truthy Value

```python
>>> first_true([False, "", None, "hello"], None)
'hello'
```

**Explanation**:

-   `None` predicate defaults to `bool()`.
-   Skips `False, "", None` (all **falsy**).
-   Returns `"hello"` (first **truthy** value).

---

### Example 3: Handling Empty Lists

```python
>>> first_true([], lambda x: x > 0)
None
```

**Explanation**:

-   The iterable is empty → **no elements to check** → returns `None`.

---

### Example 4: Finding the First Even Number

```python
>>> first_true([1, 3, 5, 6, 7], lambda x: x % 2 == 0)
6
```

**Explanation**:

-   Skips `1, 3, 5` (**odd numbers**).
-   Returns `6` (**first even number**).

---

### Example 5: Finding the First Positive Number

```python
>>> first_true([-2, -1, 0, 1, 2], lambda x: x > 0)
1
```

**Explanation**:

-   Skips `-2, -1, 0` (**not greater than 0**).
-   Returns `1` (first **positive** number).

---

## Usage 📦

Use `first_true()` to efficiently find **the first matching element** in an iterable.

```python
words = ["", "", "OpenAI", "GPT"]
result = first_true(words, lambda x: len(x) > 2)
print(result)  # Output: "OpenAI"
```

---

## Conclusion 🚀

`first_true()` is an efficient way to **search for the first matching element** while avoiding unnecessary iterations.
It **preserves order** and **handles edge cases** like empty lists or missing matches. 💡

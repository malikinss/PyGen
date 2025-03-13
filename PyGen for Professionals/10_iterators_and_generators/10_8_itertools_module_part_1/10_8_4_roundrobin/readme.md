# `roundrobin()`: Round-Robin Iterator Across Multiple Iterables

## Description 📝

The `roundrobin()` function takes multiple iterables and generates an iterator that cycles through all the iterables in a round-robin fashion, yielding the first element of each, then the second element of each, and so on.

## Purpose 🎯

This function is useful when you need to combine several iterables and alternate between them while maintaining the order of their elements.

## How It Works 🔍

1. **Creates iterators for each iterable**:  
   The function converts each input iterable into an iterator.
2. **Cycles through iterables in round-robin fashion**:

    - Yields the first element from each iterable, then the second, and so on.
    - Stops when all iterables are exhausted.

3. **Preserves the original order**:  
   Each element of the iterables is yielded in its original order.

## Output 📜

An **iterator** that produces elements in round-robin order from all input iterables.

### Example:

```python
>>> list(roundrobin([1, 2], ['a', 'b'], [True, False]))
[1, 'a', True, 2, 'b', False]
```

### Example: With Unequal Lengths

```python
>>> list(roundrobin([1, 2], ['a', 'b'], [True, False, 'c']))
[1, 'a', True, 2, 'b', False, 'c']
```

## Usage 📦

1. Call `roundrobin(*iterables)` with any number of iterables as arguments.
2. The function will return an iterator that can be consumed using `next()` or iterated over with a loop.

```python
iterators = roundrobin([1, 2], ['a', 'b'], [True, False])
for element in iterators:
    print(element)
# Output: 1, 'a', True, 2, 'b', False
```

## Conclusion 🚀

The `roundrobin()` function allows for **interleaving multiple iterables** in a clean and efficient way while preserving their original order, making it perfect for tasks that require balanced traversal of various sources. 🔄

# Lesson 6.2: Sequence Protocol 📋

## Description 📝

This lesson covers:

-   Magic method **`__len__()`** for sequence length
-   Magic methods **`__getitem__()`**, **`__setitem__()`**, and **`__delitem__()`** for indexing
-   Magic method **`__contains__()`** for membership testing
-   Practical implementation of the sequence protocol

This lesson includes a detailed theoretical explanation, 9 programming practical tasks, and 8 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to implement sequence behavior using magic methods  
✅ Create custom sequences with indexing, length, and membership operations  
✅ Apply the sequence protocol to diverse scenarios like sparse arrays and mutable strings  
✅ Build sequence-like objects that integrate with Python’s ecosystem

## Concepts & Theory 🔍

### 🔹 **`__len__()`** Magic Method

-   **Purpose**: Returns the length of a sequence, invoked by `len()`.
-   **When Used**: To define how many elements a sequence contains.

### 🔹 **`__getitem__()`**, **`__setitem__()`**, **`__delitem__()`** Magic Methods

-   **Purpose**: Handle accessing (`obj[i]`), setting (`obj[i] = val`), and deleting (`del obj[i]`) elements.
-   **When Used**: To support indexing and slicing like built-in sequences.

### 🔹 **`__contains__()`** Magic Method

-   **Purpose**: Defines membership testing, invoked by `in`.
-   **When Used**: To check if an element exists in a sequence efficiently.

## Practical Task 🧪

### 1️⃣ **Custom Sequences**

The lesson includes 9 practical tasks, each implementing sequence behavior:

1. **`ReversedSequence` Class**: Reverses a sequence’s access order.

    - Reflects changes in the original sequence, maps index `0` to last element.

2. **`SparseArray` Class**: Stores non-default elements efficiently.

    - Uses dictionary for defined indices, returns `default` for others.

3. **`CyclicList` Class**: Cycles elements infinitely.

    - Supports `append()`, `pop()`, cyclic indexing, and iteration.

4. **`SequenceZip` Class**: Combines sequences into tuples.

    - Mimics `zip()`, supports `len()`, iteration, and indexing.

5. **`OrderedSet` Class**: Maintains unique elements in insertion order.

    - Supports `add()`, `discard()`, `in`, and equality with sets/`OrderedSet`.

6. **`PermaDict` Class**: Dictionary with immutable keys.

    - Blocks value changes for existing keys, supports standard dict operations.

7. **`HistoryDict` Class**: Tracks value history per key.

    - Provides `history()` and `all_history()` for auditing changes.

8. **`MutableString` Class**: Editable string buffer.

    - Supports indexing, slicing, concatenation, and in-place case changes.

9. **`Grouper` Class**: Groups elements by key function.
    - Supports `add()`, `group_for()`, iteration, and indexing of groups.

💡 These tasks showcase versatile sequence implementations for real-world use.

## Benefits ✅

-   **`__len__()`** ensures sequences report size correctly.
-   Indexing methods enable intuitive element access and modification.
-   **`__contains__()`** optimizes membership checks.
-   Sequence protocol integrates custom objects with Python’s looping and slicing.

## Output 📜

After completing this lesson, I now:  
✅ Implement custom sequences with full indexing support  
✅ Use sequence protocol for efficient data structures  
✅ Apply sequence behavior to practical examples like ordered sets and history tracking

## Conclusion 🚀

Mastering the sequence protocol with **`__len__()`**, **`__getitem__()`**, and related methods empowers me to create powerful, Pythonic objects.  
From cyclic lists to immutable dictionaries, these tools enable intuitive, efficient data handling for diverse applications. 🧑‍💻✨

# Sorting Russian Words by Length and Lexicographic Order

## Description

This program sorts a list of **Russian words** based on:

1. **Word length** (ascending order).
2. **Lexicographic order** (if lengths are equal).

## Purpose

The goal is to **practice sorting with multiple criteria** in Python, using a lambda function as the sorting key.

## How It Works

1. **Sorting Criteria**:
    - Sort words **by length** first.
    - If lengths are equal, sort **alphabetically**.
2. **Implementation**:
    - Use `sorted()` with `key=lambda word: (len(word), word)`.
    - Join sorted words into a **single string separated by spaces**.

## Output Example

```
год раз вид мир дом день друг глаз рука лицо слово время деньги женщина работа вопрос голова ребенок система страна случай город сторона отношение часть конец человек жизнь дело место
```

## Usage

1. **Define the `data` list** with Russian words.
2. **Apply `sorted()`** with a tuple `(word length, word)`.
3. **Print the sorted words** on one line.

## Conclusion

This program effectively demonstrates **sorting with multiple criteria** using Python’s `sorted()` function and lambda functions.

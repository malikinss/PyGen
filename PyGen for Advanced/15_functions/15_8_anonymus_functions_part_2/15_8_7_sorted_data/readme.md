# Sorting US States by Last Letter

## Description

This program sorts a list of US states and their populations **in descending order based on the last character of the state name**.
If two states have the same last character, their original order is preserved.

## Purpose

The goal is to practice **custom sorting** in Python using `sorted()` with a **lambda function as the sorting key**.

## How It Works

1. **Sorting Criteria**:

    - Extract the last character of the state name.
    - Sort in **descending lexicographic order**.
    - Maintain relative order for states with the same last letter (**stable sort**).

2. **Implementation**:
    - Use `sorted()` with `key=lambda item: item[1][-1]`.
    - Set `reverse=True` to sort in descending order.
    - Iterate over the sorted list and print results in `<State>: <Population>` format.

## Output Example

```
Vermont: 626299
Massachusetts: 7029917
West Virginia: 1805832
California: 39865590
Georgia: 10711908
Tennessee: 6910840
Ohio: 11799448
Michigan: 10077331
Washington: 7705281
Arizona: 7151502
Hawaii: 1420491
Alabama: 4887871
New York: 19542209
Virginia: 10439388
```

## Usage

1. **Define the `data` list** with tuples containing `(population, state name)`.
2. **Apply `sorted()`** with a lambda function extracting the last letter.
3. **Print each state and its population** in the required format.

## Conclusion

This program demonstrates how to use **custom sorting with lambda functions** while maintaining list stability in Python.

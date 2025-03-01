# Custom zip_longest Function

## Description 📝

This Python script implements a custom `zip_longest()` function, which combines elements from multiple iterables into tuples.
Unlike the built-in `zip()` function, `zip_longest()` ensures that all elements are paired, filling in missing values from shorter iterables with a specified `fill` value.

## Purpose 🎯

The purpose of this program is to explore working with iterables of different lengths and ensure all elements are included in the output.
It helps in understanding:

-   The `zip()` function and its limitations.
-   Handling sequences of different lengths.
-   Using list comprehensions and iteration to construct a structured output.

## How It Works 🔍

1. **TODO Comment**: Describes the implementation of `zip_longest()`, highlighting how it handles sequences of different lengths.
2. **find_max_length() Function**: Determines the maximum length among the provided iterables.
3. **zip_longest() Function**:
    - Iterates over the range of the longest iterable.
    - Constructs tuples by picking elements from each iterable.
    - Fills missing elements with the specified `fill` value.
4. **Error Handling**: Ensures that all provided arguments are iterable.
5. **Example Execution**: Demonstrates how the function behaves with different input lengths.

## Output 📜

When the script is executed with the test case:

```python
print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
```

The expected output is:

```
[(1, 'a'), (2, 'b'), (3, 'c'), (4, '_'), (5, '_')]
```

## Usage 📦

1. Save the code to a file named `zip_longest.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```
    python zip_longest.py
    ```
5. Observe the output, which displays tuples combining elements from the provided lists, filling in missing values where necessary.

## Conclusion 🚀

This implementation of `zip_longest()` extends the functionality of `zip()`, allowing flexible handling of iterables with different lengths.
It showcases key programming concepts such as iteration, list comprehensions, and handling optional arguments.

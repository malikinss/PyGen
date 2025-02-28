# Weekday Name Retriever

## Description 📝

This program defines the `get_weekday()` function, which returns the full name of a day of the week in Russian based on a given integer (from 1 to 7). It also includes error handling for invalid inputs.

## Purpose 🎯

The function allows users to retrieve the name of a weekday based on its numerical representation while ensuring that invalid inputs are properly handled through exceptions.

## How It Works 🔍

1. The function takes an integer `number` as an argument.
2. It checks if the input is an integer:
    - If not, a `TypeError` is raised with the message `"The argument is not an integer"`.
3. It verifies that the number is within the valid range (1 to 7):
    - If not, a `ValueError` is raised with the message `"The argument does not belong to the required range"`.
4. If the input is valid, the function returns the corresponding day of the week in Russian.

## Output 📜

-   If a valid number is provided (e.g., `1` for "Понедельник"), the corresponding weekday is returned.
-   If the input is not an integer, an error is raised:
    ```python
    TypeError: The argument is not an integer
    ```
-   If the input is an integer but out of range, an error is raised:
    ```python
    ValueError: The argument does not belong to the required range
    ```

## Usage 📦

1. Call the function with an integer between `1` and `7`.
2. It returns the full name of the corresponding day of the week in Russian.

Example:

```python
print(get_weekday(3))
```

Output:

```text
Среда
```

Example with invalid input:

```python
print(get_weekday(9))
```

Raises:

```text
ValueError: The argument does not belong to the required range
```

## Conclusion 🚀

The `get_weekday()` function is a reliable way to retrieve the names of weekdays in Russian while ensuring input validity through proper error handling.

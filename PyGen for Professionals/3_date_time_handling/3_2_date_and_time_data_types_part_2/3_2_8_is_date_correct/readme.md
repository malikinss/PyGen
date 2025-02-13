# Validate Date Function

## Description 📝

This function checks whether a given date (day, month, and year) is valid or not.
It uses Python's `datetime.date` to validate the input and returns `True` if the date is valid and `False` if it is not.

## Purpose 🎯

The purpose of this function is to ensure that a date is correctly formatted and that the given day, month, and year actually form a valid date in the Gregorian calendar.

## How It Works 🔍

1. The function receives three arguments: `day`, `month`, and `year`.
2. It tries to create a `date` object using Python's `datetime` module with the provided values.
3. If the date is valid, the function returns `True`.
4. If the date is invalid (e.g., February 30th or April 31st), it raises a `ValueError`, and the function returns `False`.

## Output 📜

-   `True`: If the date is valid.
-   `False`: If the date is invalid.

### Example Usage:

```python
# Valid date
is_correct(29, 2, 2024)  # Returns: True

# Invalid date (February 30th)
is_correct(30, 2, 2024)  # Returns: False

# Invalid date (April 31st)
is_correct(31, 4, 2024)  # Returns: False
```

## Usage 📦

1. The function `is_correct(day, month, year)` takes three arguments: `day`, `month`, and `year`.
2. It returns `True` if the date is valid, otherwise `False`.

## Conclusion 🚀

This function provides an easy way to validate whether a given day, month, and year form a legitimate date, making it a useful utility for date validation tasks.

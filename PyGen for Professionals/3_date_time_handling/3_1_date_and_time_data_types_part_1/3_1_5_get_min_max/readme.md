# Get Minimum and Maximum Dates

## Description 📝

The `get_min_max()` function finds the earliest and latest dates from a given list of dates.
If the list is empty, it returns an empty tuple.

## Purpose 🎯

This function helps in determining the range of dates from a dataset, which can be useful for historical analysis, tracking events, or setting date boundaries.

## How It Works 🔍

1. The function checks if the list of dates is empty.
2. If the list is not empty, it calculates the minimum and maximum dates using the `min()` and `max()` functions.
3. It returns a tuple where:
    - The first element is the earliest date.
    - The second element is the latest date.
4. If the list is empty, it returns an empty tuple.

## Output 📜

Example output when calling the function:

```python
(1999-04-14, 2021-10-11)
```

## Usage 📦

1. Provide a list of `date` objects.
2. Call the `get_min_max()` function with the list.
3. The function returns a tuple containing the minimum and maximum dates, or an empty tuple if the list is empty.

## Conclusion 🚀

The `get_min_max()` function is a simple and efficient way to find the date range within a given list of dates, making it useful for data analysis and historical records management.

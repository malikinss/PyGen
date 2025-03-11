# Generate All Dates in a Year

## Description 📝

The `years_days()` function is a generator that yields all the dates in a given year.
Starting from January 1st to December 31st, it generates each date in sequence, making it possible to iterate over the entire year day by day.

## Purpose 🎯

This function is useful for iterating over all the days in a year, whether for date-related calculations, processing logs, or other date-based operations.
The generator makes it memory-efficient to handle even large date ranges by yielding one date at a time.

## How It Works 🔍

1. **Input Parameters**:
    - `year`: A natural number representing the year for which to generate all dates.
2. **Generator**:

    - The function uses a generator to yield each date starting from January 1st of the given year until December 31st.
    - The generator makes use of Python's `datetime` module, specifically the `date` and `timedelta` classes, to iterate over the year day by day.

3. **Date Calculation**:
    - The generator starts with January 1st (`date(year, 1, 1)`).
    - It yields the current date and increments the date by one day using `timedelta(days=1)`.

## Output 📜

The function yields a sequence of `date` objects, each representing a day in the year. You can iterate over these dates or convert them to strings for display.

### Example:

```python
>>> for d in years_days(2022):
>>>     print(d)
2022-01-01
2022-01-02
2022-01-03
...
2022-12-31
```

## Usage 📦

1. Save the code to a file, e.g., `generate_dates.py`.
2. Call the function `years_days()` with the desired year:
    ```python
    for d in years_days(2022):
        print(d)  # Outputs each date in 2022
    ```

## Conclusion 🚀

The `years_days()` generator provides an efficient way to iterate over all the days in a specific year.
Using a generator ensures low memory consumption while processing a full year's worth of dates. 🎉

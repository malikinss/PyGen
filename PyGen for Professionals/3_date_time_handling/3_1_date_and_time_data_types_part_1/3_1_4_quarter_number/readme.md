# Print Year and Quarter for Dates

## Description 📝

The `print_year_and_quarter()` function takes a list of dates and prints the year along with the corresponding quarter for each date in the list.
The quarter is determined by the month of the date.

## Purpose 🎯

This function is useful for determining the fiscal or calendar quarter in which specific dates fall.
It processes each date in the list and outputs the year and quarter.

## How It Works 🔍

1. The function iterates over each date in the input list.
2. For each date, the month is passed to the `get_quarter()` function to determine the quarter.
3. The result is printed in the format `YYYY-QX`, where `X` is the quarter number.

## Output 📜

Example output when running the function:

```python
2010-Q3
2017-Q1
2009-Q4
2010-Q1
2021-Q4
2020-Q1
2000-Q3
1999-Q2
1789-Q4
2013-Q3
1666-Q2
1968-Q2
```

## Usage 📦

1. Define a list of `date` objects.
2. Call the `print_year_and_quarter()` function with the list of dates.
3. The function prints the year and quarter for each date in the list.

## Conclusion 🚀

This function is helpful for categorizing dates into specific fiscal or calendar quarters, which can be useful in various applications such as data analysis, finance, or reporting.

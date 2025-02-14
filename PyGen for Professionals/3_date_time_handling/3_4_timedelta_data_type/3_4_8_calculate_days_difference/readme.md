# Date Difference Calculator 📅

## Description 📝

This program calculates the number of days between two adjacent dates in a given sequence.
It returns a list of nonnegative integers, each representing the absolute difference in days between two consecutive dates.
If the sequence consists of a single date, the program will output an empty list.

## Purpose 🎯

The program allows the user to input a sequence of dates, and it calculates the absolute difference in days between each pair of adjacent dates.

## How It Works 🔍

1. The user inputs a sequence of dates in the "DD.MM.YYYY" format.
2. The program calculates the absolute number of days between each adjacent date pair in the sequence.
3. The program outputs the results as a list of integers.
4. If only one date is provided, an empty list is returned.

### Example:

```python
user_dates = get_user_dates()  # e.g., ['01.01.2025', '05.01.2025', '10.01.2025']
days_diff = calculate_days_difference(user_dates)
print(days_diff)
```

## Output 📜

The program will output a list of non-negative integers representing the number of days between consecutive dates.

### Example output:

```
[4, 5]
```

For the dates `01.01.2025`, `05.01.2025`, and `10.01.2025`, the program will output the differences: 4 days between the first and second date, and 5 days between the second and third date.

## Usage 📦

1. Input a sequence of dates separated by spaces in the format "DD.MM.YYYY".
2. The program will display a list of the number of days between adjacent dates.

## Conclusion 🚀

This program is useful for calculating the time gaps between dates in any given sequence, regardless of the order in which the dates are entered.

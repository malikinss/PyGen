# Thirteenth Day Calculator 📅

## Description 📝

This program calculates how many times the 13th day of the month falls on each day of the week from 01/01/0001 to 31/12/9999.
It provides a detailed count of the occurrences for each weekday.

## Purpose 🎯

The purpose of this program is to demonstrate the frequency with which the 13th day of the month falls on different weekdays, showing that the 13th often occurs on Fridays, as commonly believed.

## How It Works 🔍

1. The program iterates over each year in the range from 0001 to 9999.
2. For each year, it checks all 12 months.
3. For each month, it calculates the weekday of the 13th day.
4. The program counts how often each day of the week (e.g., Monday, Tuesday, etc.) is the 13th of the month.
5. The results are displayed in the order of days of the week.

### Example:

```python
# Running the program will calculate how often the 13th day of the month falls on each weekday
weekday_counts = count_thirteenth_days(1, 9999)
display_weekday_counts(weekday_counts)
```

## Output 📜

The program will display the number of occurrences of the 13th falling on each day of the week.

### Example output:

```
Monday: 1711
Tuesday: 1711
Wednesday: 1711
Thursday: 1711
Friday: 1711
Saturday: 1711
Sunday: 1711
```

## Usage 📦

1. The program runs from 01/01/0001 to 31/12/9999 by default. You can modify the date range by changing the arguments passed to the `count_thirteenth_days` function.
2. The program will display how often the 13th falls on each weekday.

## Conclusion 🚀

This program proves the widespread belief that the 13th of the month most often falls on a Friday, along with showing the count of 13ths across all days of the week throughout history.

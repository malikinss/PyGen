# Find Interesting Dates

## Description 📝

This program takes a list of dates and outputs the "interesting" ones in ascending order.
A date is considered interesting if its year coincides with the user's year of birth, and the sum of the month number and day number equals the user's age.
The dates are displayed in the format `Month DD, YYYY`.

## Purpose 🎯

The purpose of this program is to filter and display dates that meet specific criteria (matching the user's year of birth and the sum of month and day equal to their age).
The dates are shown in a human-readable format.

## How It Works 🔍

1. The program first checks each date to see if it is "interesting."
2. A date is considered interesting if:
    - The year matches the user's year of birth.
    - The sum of the month number and day number equals the user's age.
3. All "interesting" dates are sorted in ascending order.
4. The program then outputs these dates in the format `Month DD, YYYY`.

## Output 📜

For example, if the input list contains the following dates:

```
1992-06-25
1992-03-01
1992-09-29
```

The program will output:

```
March 01, 1992
June 25, 1992
```

## Usage 📦

1. The function `print_good_dates(dates)` takes a list of date objects as input.
2. The function will print all "interesting" dates in ascending order in the format `Month DD, YYYY`.

## Conclusion 🚀

This program efficiently filters and formats interesting dates, allowing for easy identification of dates that hold personal significance based on predefined conditions.

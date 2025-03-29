# Python Meetup Date Finder 🗓️

## Description 📝

The program determines the date of the fourth Thursday of a given month and year, which is when the Python meetup in San Diego takes place.
It calculates the date based on the provided year and month and outputs it in the format `DD.MM.YYYY`.

## Purpose 🎯

This program helps determine the exact date of the Python meetup in San Diego for any given month and year.
By calculating the fourth Thursday of a month, it ensures the correct date for the meetup.

## How It Works 🔍

1. The program reads the year and month as input.
2. It calculates the first day of the given month and checks which weekday it falls on.
3. Using this information, it determines the date of the first Thursday of the month.
4. Then, it adds 21 days to find the fourth Thursday of that month.
5. The final result is formatted in the `DD.MM.YYYY` format.

## Output 📜

The program outputs the date of the fourth Thursday of the given month in the format `DD.MM.YYYY`.

## Usage 📦

1. Provide the year and month as input, one per line.
2. The function will calculate and print the date of the fourth Thursday of that month in the required format.

### Example:

```python
2025
05
```

Output:

```
22.05.2025
```

## Conclusion 🚀

This program efficiently calculates the date of the Python meetup by determining the fourth Thursday of any given month and year.

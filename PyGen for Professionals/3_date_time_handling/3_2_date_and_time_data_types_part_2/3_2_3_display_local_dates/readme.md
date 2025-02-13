# First Hurricane Date Formatter

## Description 📝

The `print_hurricane_first_date()` function extracts the earliest date from a list of Florida hurricane occurrences and prints it in three different formats.

## Purpose 🎯

This function is useful for displaying historical hurricane data in multiple formats, catering to different regional date conventions.

## How It Works 🔍

1. The function receives a list of `date` objects representing hurricane occurrences.
2. It determines the earliest date from the list.
3. It formats and prints this date in:
    - ISO standard format (`YYYY-MM-DD`)
    - Russian format (`DD.MM.YYYY`)
    - American format (`MM/DD/YYYY`)

## Output 📜

Example output for the hurricane dates `[1992-08-24, 2000-07-07, 2010-09-28]`:

```
Date of first hurricane in ISO format: 1992-08-24
Date of first hurricane in RU format: 24.08.1992
Date of first hurricane in US format: 08/24/1992
```

## Usage 📦

1. Prepare a list of `date` objects representing hurricane occurrences.
2. Pass this list to `print_hurricane_first_date()`.
3. The function determines the earliest hurricane date and prints it in three formats.

## Conclusion 🚀

The `print_hurricane_first_date()` function provides a convenient way to display historical hurricane dates in multiple regional formats, making it easier to interpret and analyze data across different conventions.

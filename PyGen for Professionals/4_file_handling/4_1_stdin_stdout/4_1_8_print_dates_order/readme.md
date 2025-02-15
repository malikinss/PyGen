# Date Sequence Order Checker

## Description 📝

This Python program reads a sequence of dates, checks their order, and outputs whether the dates appear in strictly ascending order, strictly descending order, or a mixed order.
The program helps to analyze the order of dates for given sequences in an efficient manner.

## Purpose 🎯

The purpose of this program is to determine the order of a sequence of dates, providing clarity on whether the dates are in ascending, descending, or mixed order.

## How It Works 🔍

1. **Function `read_input()`**:

    - Reads input data from the standard input and returns a list of stripped date strings.

2. **Function `string_to_date(date_string)`**:

    - Converts a date string in the format `DD.MM.YYYY` into a `date` object.

3. **Function `parse_dates(data)`**:

    - Parses the input date strings into a list of `date` objects.

4. **Function `check_order(dates)`**:

    - Determines whether the list of dates is in strictly ascending order, strictly descending order, or mixed order.

5. **Function `print_dates_order(dates)`**:
    - Prints the result, which can be "ASC" (ascending), "DESC" (descending), or "MIX" (mixed).

### Example:

For input:

```
01.01.2020
02.01.2020
03.01.2020
```

The program will output:

```
ASC
```

## Output 📜

The program outputs one of the following:

-   "ASC" if the dates are in strictly ascending order.
-   "DESC" if the dates are in strictly descending order.
-   "MIX" if the dates are in neither ascending nor descending order.

Example output:

```
ASC
```

## Usage 📦

1. Save the code in a file named `date_sequence_checker.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script and provide input via standard input.

### Example usage:

```bash
$ python date_sequence_checker.py
01.01.2020
02.01.2020
03.01.2020
```

The output will be:

```
ASC
```

## Conclusion 🚀

This program efficiently determines and displays the order of a given sequence of dates.
It is a useful tool for quickly verifying if a list of dates is arranged in ascending or descending order.

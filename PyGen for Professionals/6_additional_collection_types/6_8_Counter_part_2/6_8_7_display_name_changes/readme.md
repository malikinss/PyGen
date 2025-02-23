# User Name Change Tracker

## Description 📝

This Python program analyzes a CSV file (`name_log.csv`) that logs user name changes while keeping their email addresses unchanged.
The program determines how many times each user has changed their name and displays the results in lexicographic order.

## Purpose 🎯

The goal of this program is to efficiently count and display the number of times each user has changed their name using their email as a unique identifier.
This is useful for tracking account modifications and monitoring user behavior.

## How It Works 🔍

1. The program reads a CSV file containing three columns:
    - `username` (changed user name)
    - `email` (unique user email)
    - `dtime` (timestamp of the name change)
2. It processes the file and counts the occurrences of each email.
3. The email addresses are sorted in lexicographic order.
4. The program then prints each email alongside the number of name changes.

## Output 📜

The program outputs email addresses and the corresponding number of name changes in the format:

```
<email address>: <number of name changes>
```

### Example:

#### CSV Input (`name_log.csv`):

```
username,email,dtime
rare_charles6,charlesthompson@inbox.ru,11/15/2021 08:15
busy_patricia5,patriciasmith@bk.ru,11/07/2021 08:07
charles_t,charlesthompson@inbox.ru,11/20/2021 10:45
patricia_s,charlesthompson@inbox.ru,11/23/2021 15:30
```

#### Program Output:

```
charlesthompson@inbox.ru: 3
patriciasmith@bk.ru: 1
```

## Usage 📦

1. Ensure the CSV file (`name_log.csv`) exists in the specified directory.
2. Run the program with Python.
3. The results will be printed to the console.

### Running the script:

```bash
python script.py
```

## Conclusion 🚀

This program provides a simple yet effective way to track user name changes based on email addresses.
It ensures data integrity and enables easy analysis of account modifications.

# Sort and Display Email Addresses 📧

## Description 📝

This program takes a dictionary where email addresses are grouped by domain, extracts all email addresses, sorts them in alphabetical order, and prints each email on a separate line in the format `username@domain`.

## Purpose 🎯

The purpose of this program is to display all email addresses from a given dictionary in an alphabetically sorted order.
Each email is displayed on a new line in the format `username@domain`.

## How It Works 🔍

1. **Input**:
    - A dictionary `emails` where the keys are email domains, and the values are lists of usernames associated with that domain.
2. **Processing**:
    - The program generates a list of full email addresses by concatenating usernames with their corresponding domains.
    - The list of email addresses is sorted alphabetically using Python's `sorted()` function.
3. **Output**:
    - The email addresses are printed on separate lines in sorted order.

## Output 📜

The program outputs the email addresses in alphabetical order.

### Example Input/Output:

**Input**:

```python
emails = {
    'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
    'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
    'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
    'yandex.ru': ['surface', 'google'],
    'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
    'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']
}
```

**Output**:

```text
angel.down@mail.ru
beegeek@msu.edu
beegeek.school@msu.edu
cream.soda@hse.edu
google@yandex.ru
joanne@mail.ru
joseph@nosu.edu
larisa.mamuk@nosu.edu
rustam.mini@gmail.com
ruslan.chaika@gmail.com
stepik-best@gmail.com
svetlana.gaeva@nosu.edu
surface@yandex.ru
tomas-henders@hse.edu
zivert@hse.edu
apple.fruit@msu.edu
```

## Usage 📦

1. Copy the code into a Python file (e.g., `print_sorted_emails.py`).
2. Pass the dictionary `emails` to the `print_sorted_emails()` function.
3. The function will print all email addresses in alphabetical order, each on a separate line.

### Example Run:

```python
# Sample run
emails = {
    'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
    'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
    'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
    'yandex.ru': ['surface', 'google'],
    'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
    'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']
}

print_sorted_emails(emails)
```

**Output**:

```text
angel.down@mail.ru
beegeek@msu.edu
beegeek.school@msu.edu
cream.soda@hse.edu
google@yandex.ru
joanne@mail.ru
joseph@nosu.edu
larisa.mamuk@nosu.edu
rustam.mini@gmail.com
ruslan.chaika@gmail.com
stepik-best@gmail.com
svetlana.gaeva@nosu.edu
surface@yandex.ru
tomas-henders@hse.edu
zivert@hse.edu
apple.fruit@msu.edu
```

## Conclusion 🚀

This program effectively handles the task of displaying email addresses in an organized and alphabetical manner, providing a simple solution to work with grouped email data.

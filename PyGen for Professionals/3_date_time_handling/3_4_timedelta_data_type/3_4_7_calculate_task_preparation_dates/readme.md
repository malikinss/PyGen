# Task Preparation Dates 📅

## Description 📝

This program helps Arthur prepare tasks for his "OOP in Python" course by calculating the dates on which he should prepare each task.
The preparation schedule follows a specific rule: each subsequent task takes one more day than the previous one.

## Purpose 🎯

The program calculates the dates when Arthur should prepare each of the 10 tasks, starting from a given date.
The first task is prepared the same day, the second in one day, the third in two days, and so on.

## How It Works 🔍

1. The user inputs a start date.
2. The program calculates the preparation dates for 10 tasks.
3. Each subsequent task is due one more day later than the previous one.
4. The program outputs the list of dates in "DD.MM.YYYY" format.

### Example:

```python
start_date = get_user_date()  # e.g., 01.01.2025
task_dates = calculate_task_dates(start_date)
display_dates(task_dates)
```

## Output 📜

The program will output the dates on which each task should be prepared.

### Example output:

```
01.01.2025
03.01.2025
06.01.2025
10.01.2025
15.01.2025
21.01.2025
28.01.2025
36.01.2025
45.01.2025
55.01.2025
```

## Usage 📦

1. Input the start date in the format "DD.MM.YYYY".
2. The program will display the preparation dates for 10 tasks.

## Conclusion 🚀

This program provides a simple and effective way for Arthur to manage his task preparation schedule, ensuring he is never overwhelmed by a too-tight timeline.

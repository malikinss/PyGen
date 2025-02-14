# Task Duration Calculator ⏱️

## Description 📝

This program calculates the total time spent on solving various tasks.
Each task has a recorded start and end time, and the program computes the total duration spent on all tasks in minutes.
The times are provided as strings in the "HH:MM" format.

## Purpose 🎯

The purpose of this program is to help programmers track the time spent solving tasks, which can be useful for productivity tracking, time management, or performance analysis.

## How It Works 🔍

1. The program takes a list of task records, where each record is a tuple containing the start time and the end time of a task in "HH:MM" format.
2. The program converts these times into `datetime` objects and calculates the duration for each task.
3. The total duration of all tasks is then computed in minutes and displayed.

### Example:

```python
# Example data:
data = [
    ('07:14', '08:46'),
    ('09:01', '09:37'),
    ('10:00', '11:43'),
    ('12:13', '13:49'),
    ('15:00', '15:19'),
    ('15:58', '17:24'),
    ('17:57', '19:21'),
    ('19:30', '19:59')
]
# Output: The total time spent solving all problems.
```

## Output 📜

The program outputs the total time in minutes spent on all tasks.

### Example output:

```
Total minutes spent: 452
```

## Usage 📦

1. Input the task data, where each task is a tuple containing the start and end times in "HH:MM" format.
2. The program will calculate and print the total time spent in minutes.

## Conclusion 🚀

This program helps you easily calculate the total time spent on solving tasks, which can be valuable for tracking work progress, understanding time allocation, or improving productivity.

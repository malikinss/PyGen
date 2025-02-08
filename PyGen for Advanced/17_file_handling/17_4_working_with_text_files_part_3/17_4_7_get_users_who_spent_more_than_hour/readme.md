# User Login Duration Program

## Description 📝

This Python program processes a log file named `logfile.txt`, which contains information about users' login and logout times. The program filters out users who have been online for at least one hour and writes their names to `output.txt`. Each entry in the log file includes a user name, entry time, and exit time, all in 24-hour format.

## Purpose 🎯

The purpose of this program is to extract and filter users based on their online duration from a log file. It then generates an output file containing only the users who have been logged in for at least one hour.

## How It Works 🔍

1. **Reading Data**:
    - The `read_data_from_file()` function reads the log file and returns its content as a list of lines.
2. **Converting Data**:
    - Each line from the log file is processed by the `convert_row_to_list()` function, which splits the line by commas and returns a list of `[user_name, entry_time, exit_time]`.
3. **Time Calculation**:
    - The `convert_str_time_to_int_min()` function converts the entry and exit times from "HH:MM" format into total minutes.
    - The `get_minutes_difference()` function calculates the difference in minutes between the entry and exit times.
4. **Filtering Users**:
    - The `get_users_who_spent_more_than_hour()` function filters the users whose online time is at least 60 minutes.
5. **Writing Output**:
    - The `write_data_to_file()` function writes the filtered list of users to `output.txt`, with each user on a new line.

## Output 📜

The program creates or overwrites the `output.txt` file, which contains the names of users who have been logged in for at least one hour. Each user name is written on a separate line.

For example, if the `logfile.txt` file contains:

```
user1, 09:00, 10:30
user2, 08:30, 09:15
user3, 10:00, 11:05
```

The resulting `output.txt` will contain:

```
user1
user3
```

## Usage 📦

1. Save the code in a file, e.g., `filter_users_by_duration.py`.
2. Ensure that the `logfile.txt` file is available in the same directory as the program.
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script using the command:
   `python filter_users_by_duration.py`
6. The program will read the `logfile.txt`, filter the users who have been online for at least one hour, and generate the `output.txt` file.

## Conclusion 🚀

This program effectively filters users based on their login duration and generates a list of users who were online for at least one hour. It demonstrates basic file processing, string manipulation, and time calculation in Python.

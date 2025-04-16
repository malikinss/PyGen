Lesson 6.3: with operator

Resource Management in Python
with operator
Abstract: This lesson is about the with operator.

https://stepik.org/lesson/810855/step/1?unit=816646

This lesson has good theory explonation, has 3 programing practical tasks and 11 theoretical questions presented on the website.

6_3_with_operator
├───6_3_1_print_file_content
├───6_3_2_non_closed_files
└───6_3_3_log_for

1. 6_3_1_print_file_content

```
# print_file_content Function File Display Utility
The `print_file_content` function accepts a `filename` parameter, a string representing a text file’s name (including extension).
It prints the file’s contents using UTF-8 encoding.
If the file is absent from the program’s folder, it outputs "File not found".
Designed for basic file reading tasks, such as displaying logs, configurations, or text data in scripts or command-line tools.
Error handling ensures clear feedback for missing files, fitting automation, debugging, or educational file I/O demonstrations.
```

2. 6_3_2_non_closed_files

```
# non_closed_files Function Open File Filter
The `non_closed_files` function accepts a list of file objects (`files`) and returns a new list containing only the open file objects, preserving their original order from the input list.
Designed for scenarios requiring identification of active file handles, such as resource management, debugging file leaks, or cleanup in applications handling multiple files.
It ensures only open files are processed, useful in scripting or system administration tasks.
```

3. 6_3_3_log_for

```
# log_for Function Date-Specific Log Extractor
The `log_for` function processes a log file to extract events for a specified date, creating a new file with these events.
It takes two arguments: `logfile` (the input log file name, including extension) and `date_str` (a date in `YYYY-MM-DD` format).
The function generates a file named `log_for_<date_str>.txt`, writing events from `logfile` that match `date_str`, omitting the date prefix, and preserving their original order, using UTF-8 encoding.
Designed for log analysis tasks, such as filtering system or application logs by date for auditing, debugging, or reporting.
The function’s focused output simplifies reviewing specific events, fitting use cases in system administration, error tracking, or educational exercises on file processing.
```

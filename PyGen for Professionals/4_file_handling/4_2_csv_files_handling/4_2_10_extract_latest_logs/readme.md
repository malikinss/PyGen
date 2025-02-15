# User Name Change Log Processor 📝

## Description 🎯

This program processes a `CSV` file containing user name change logs, extracts the most recent name change for each user, and writes the results to a new `CSV` file.
The entries are sorted by user email address in lexicographic order.

## Purpose 🎯

The purpose of this program is to:

-   Read the input `CSV` file (`name_log.csv`).
-   Select only the most recent name change for each user based on the change timestamp.
-   Write the processed data into a new `CSV` file (`new_name_log.csv`).
-   Ensure the logs are sorted by the user’s email address.

## How It Works 🔍

1. **Reading Input Data:** The program reads the `name_log.csv` file and loads it into memory.
2. **Grouping Logs by Email:** It groups the logs based on the email address.
3. **Finding the Latest Log for Each User:** For each user, the most recent log is identified by comparing the timestamp.
4. **Sorting:** The resulting logs are sorted by the user’s email in lexicographic order.
5. **Writing to Output:** The processed logs are written to the `new_name_log.csv` file.

## Output 📜

The output file `new_name_log.csv` contains the following columns:

-   `username`: The most recent username.
-   `email`: The user’s email address.
-   `dtime`: The date and time when the username was last updated.

The logs are sorted in lexicographic order based on the user’s email.

## Usage 📦

1. Ensure the input file `name_log.csv` is in the correct format with the following columns: `username,email,dtime`.
2. Run the program to process the `CSV` file and extract the most recent logs.
3. The output file `new_name_log.csv` will be created, containing only the most recent name changes for each user, sorted by email.

### Example:

Input:

```
username,email,dtime
rare_charles6,charlesthompson@inbox.ru,11/15/2021 08:15
busy_patricia5,patriciasmith@bk.ru,11/07/2021 08:07
```

Output:

```
username,email,dtime
rare_charles6,charlesthompson@inbox.ru,11/15/2021 08:15
busy_patricia5,patriciasmith@bk.ru,11/07/2021 08:07
```

## Conclusion 🚀

This program efficiently processes user name change logs, ensuring that only the most recent name changes are recorded and that the data is properly sorted for further analysis.

# Domain Usage Counting Program

## Description 📝

This program reads a `CSV` file containing user data with names, surnames, and email addresses.
It extracts the domain from the email addresses, counts the occurrences of each domain, and writes the result to a new `CSV` file, sorted by the number of domain occurrences in ascending order.
In case of a tie in domain counts, the domains are sorted lexicographically.

## Purpose 🎯

The purpose of this program is to:

-   Read a `CSV` file containing user email addresses.
-   Count how many times each domain is used.
-   Create a new `CSV` file with the domain names and their respective counts.
-   Sort the data by the number of occurrences, and lexicographically when the counts are the same.

## How It Works 🔍

1. The function `read_csv_file()` reads the original `CSV` file containing user data.
2. The function `count_domain_occurrences()` extracts the domain from the email addresses and counts how many times each domain appears.
3. The dictionary with domain counts is then converted into a list of lists using `convert_dict_to_list_of_lists()`.
4. The resulting list is sorted first by the count of occurrences, and then by the domain name (lexicographically in case of ties).
5. The final result is written to a new `CSV` file using `write_to_csv_file()`.

## Output 📜

The program generates a `CSV` file `domain_usage.csv` with the following structure:

```
domain,count
rambler.ru,24
iCloud.com,29
...
```

Where:

-   The `domain` column contains the name of the email domain.
-   The `count` column contains the number of users using that domain.

The rows are sorted in ascending order based on the domain's usage count. If multiple domains have the same usage count, they are sorted lexicographically by domain name.

## Usage 📦

1. Ensure you have a `data.csv` file with the format:

    ```
    first_name,surname,email
    John,Wilson,johnwilson@outlook.com
    Mary,Wilson,marywilson@list.ru
    ...
    ```

2. Run the program. It will:

    - Read the `data.csv` file.
    - Count domain occurrences.
    - Write the results to `domain_usage.csv`.

3. The `domain_usage.csv` file will contain the sorted list of email domains and their usage counts.

### Example:

If the `data.csv` file contains the following data:

```
first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
Tim,Green,timgreen@outlook.com
Arthur,Smith,arthursmith@icloud.com
```

The output in `domain_usage.csv` will look like:

```
domain,count
icloud.com,1
list.ru,1
outlook.com,2
```

## Conclusion 🚀

This program provides a simple yet powerful way to analyze email domain usage from a `CSV` file.
It sorts and processes the data efficiently and outputs a well-structured `CSV` file containing the domain counts.

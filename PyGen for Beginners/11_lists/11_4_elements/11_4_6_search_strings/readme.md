# Search Strings with Multiple Queries 📝

## Description 📝

This Python program allows you to search for strings that contain **all** the provided search queries at the same time. The search is case-insensitive, meaning it will match queries regardless of letter case. It is useful when you need to filter a list of strings based on multiple criteria.

## Purpose 🎯

The program helps filter out strings that meet multiple search conditions, which can be particularly useful for analyzing or searching through large datasets, logs, or text documents.

## How It Works 🔍

1. The program first reads an integer `n`, which represents the number of input strings.
2. Then, it reads the `n` strings.
3. It reads an integer `k`, which represents the number of search queries.
4. It reads `k` search queries.
5. The program searches through the `n` strings and returns only those that contain **all** search queries at once.
6. The search is case-insensitive, meaning both uppercase and lowercase versions of the search queries will be matched.

## Output 📜

```bash
Example Input:
5
Hello World
This is a test
Search for this
Hello there
Goodbye world
2
hello
world

Example Output:
Hello World
Goodbye world
```

## Usage 📦

1. Save the script as` search_strings.py`.
2. Run the script in a Python environment.
3. Input the number `n` (the number of strings).
4. Enter the `n` strings, one per line.
5. Input the number `k` (the number of search queries).
6. Enter the `k` search queries, one per line.
7. The program will print the strings that contain all the search queries.

## Conclusion 🚀

This program efficiently filters strings based on multiple search terms and is useful for data analysis, text processing, and searching through large collections of data.

# Filter and Sort Russian Names Program

## Description 📝

This Python script filters a list of Russian names based on two conditions:

1. The name must start with the letters 'A' or 'M' (case insensitive).
2. The name must have a length greater than 4 characters.

The filtered names are then sorted in lexicographic order and printed, each with its first letter capitalized.

## Purpose 🎯

The purpose of this program is to demonstrate how to filter, manipulate, and sort data in Python using functional programming techniques such as `filter()` and `map()`.
It also emphasizes string manipulation, including case handling and formatting (capitalization).

## How It Works 🔍

1. **filter_names_by_conditions()**: Filters the names based on the starting letter and length. Then, it capitalizes each name and sorts the list alphabetically.
2. **filter()**: Used to apply the conditions of starting with 'A' or 'M' and having a length greater than 4.
3. **map()**: Used to capitalize the names after they have been filtered.
4. **sorted()**: Ensures that the final list of names is in lexicographic order.

## Output 📜

The output will be the names that match the conditions, printed in lexicographic order, with the first letter of each name capitalized:

```
Adelina Alexander Amelija Andrey Artëm Artëmiy Atselina Arsen Maxim Mark Margarita Matvej
```

## Usage 📦

1. Save the code to a file named `filter_and_sort_names.py`.
2. Create a list of names, `names`, as shown in the code.
3. Open a terminal or command prompt.
4. Navigate to the directory where the file is located.
5. Execute the script using the command:
    ```
    python filter_and_sort_names.py
    ```
6. The program will output the sorted, filtered list of names.

## Conclusion 🚀

This program provides an efficient way to filter and process lists using Python's built-in functions.
It showcases how simple conditions can be applied to strings while leveraging sorting and string formatting for clean results.

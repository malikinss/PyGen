# Titanic Survivor Program

## Description 📝

This program processes a `CSV` file containing data about passengers aboard the Titanic.
It identifies the passengers who survived and were under 18 years old, and prints their names, first listing male survivors followed by female survivors.
The names are displayed in the order they appear in the original dataset.

## Purpose 🎯

The program aims to:

-   Read data from a `CSV` file containing passenger information.
-   Identify the surviving passengers who were under 18 years old.
-   Print the names of these passengers, first male then female, maintaining the original order for each group.

## How It Works 🔍

1. The function `read_csv()` reads the `CSV` file into a list of dictionaries, where each dictionary represents a passenger's information.
2. The program uses helper functions (`is_survived()`, `is_young()`, `is_male()`, and `is_female()`) to filter passengers based on their survival status, age, and gender.
3. The function `get_specific_sex_survivors_under_18()` filters the data to find survivors under 18, using a gender-specific function to sort male and female passengers.
4. The function `print_names()` prints the names of the filtered passengers.

## Output 📜

The program prints the names of the surviving passengers under 18, first listing all males, followed by all females. Each name is printed on a separate line.

### Example Output:

```
Master. Michael McDermott:
Master. William Thompson:
Miss. Sally Ann Wells:
...
```

## Usage 📦

1. Ensure you have a `titanic.csv` file with the format:

    ```
    survived;name;sex;age
    0;Mr. Owen Harris Braund;male;22
    1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
    ...
    ```

2. Run the program, which will:
    - Read the `titanic.csv` file.
    - Filter out passengers under 18 who survived.
    - Print their names, first for males and then females.

## Conclusion 🚀

This program provides a useful way to identify and list survivors under 18 from the Titanic dataset.
It outputs the results in an ordered and structured way, making it easy to analyze the data.

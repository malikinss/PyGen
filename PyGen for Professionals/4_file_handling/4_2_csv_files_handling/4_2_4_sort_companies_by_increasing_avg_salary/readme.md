# Sorted Companies by Average Salary Program

## Description 📝

This Python script processes employee salary data from a `CSV` file (`salary_data.csv`) and sorts companies based on the average salary of their employees.
If two companies have the same average salary, they are ordered alphabetically by their names.
The program helps to analyze and compare companies based on their employee compensation.

## Purpose 🎯

The program reads a `CSV` file containing employee salary data, calculates the average salary for each company, and sorts the companies in ascending order of average salary.
If two companies have the same average salary, they are sorted alphabetically.
This could be useful for analyzing salary distributions across different companies.

## How It Works 🔍

1. **read_csv_data() Function**: Reads the `CSV` file and returns a list of tuples, each containing the company name and salary.
2. **compute_average_value() Function**: Computes the average salary for a list of salaries.
3. **group_salaries_by_company() Function**: Groups salaries by company.
4. **compute_average_salaries() Function**: Computes the average salary for each company.
5. **sort_companies_by_avg_salary() Function**: Sorts companies first by average salary in ascending order and then alphabetically if the salaries are the same.
6. **display_sorted_companies() Function**: Displays the sorted list of companies.

## Output 📜

When the script is executed, it will display the names of the companies, sorted by increasing average salary:

```
HighTech
Inline Group
IBS
Atos
Philax
Oracle
```

## Usage 📦

1. Save the code to a file named `sort_companies_by_avg_salary.py`.
2. Create a `CSV` file `salary_data.csv` in the same directory with the following contents:
    ```
    company_name;salary
    Atos;135000
    HighTech;24400
    Philax;128600
    Inline Group;43900
    IBS;70600
    Oracle;131600
    Atos;91000
    ```
3. Open a terminal or command prompt.
4. Navigate to the directory where the files are located.
5. Execute the script using the command:
    ```
    python sort_companies_by_avg_salary.py
    ```
6. The program will display the companies sorted by their average salary.

## Conclusion 🚀

This program provides an easy way to compare companies based on the average salary of their employees. It also handles sorting companies with the same average salary by their name in lexicographical order. This exercise demonstrates how to process `CSV` files, perform basic calculations, and sort data efficiently in Python.

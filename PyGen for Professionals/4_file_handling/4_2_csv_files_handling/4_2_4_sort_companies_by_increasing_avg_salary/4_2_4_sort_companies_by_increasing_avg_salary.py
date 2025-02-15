'''
TODO:
    You have access to the file salary_data.csv, which contains anonymous
    information about employee salaries in various companies.

    The first column contains the company name, and the second column contains
    the salary of the next employee:
        company_name;salary
        Atos;135000
        HighTech;24400
        Philax;128600
        Inline Group;43900
        IBS;70600
        Oracle;131600
        Atos;91000
        ...

    Write a program that sorts the companies by increasing average salary of
    their employees and displays their names, each on a separate line.

    If two companies have the same average salaries, they should be arranged
    in lexicographic order of their names.

NOTE:
    The average salary of a company is defined as the ratio of the sum of all
    salaries to their number.

    The separator in the file salary_data.csv is a semicolon, and quotation
    marks are not used.
'''
import csv
from collections import defaultdict
from typing import List, Tuple, Dict


def read_csv_data(filename: str) -> List[Tuple[str, int]]:
    """
    Reads employee salary data from a CSV file.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        List[Tuple[str, int]]: A list of tuples containing company names and
        salaries.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)  # Skip header
        return [(row[0], int(row[1])) for row in reader]


def compute_average_value(values: List[int]) -> float:
    """
    Computes the average of a list of numbers.

    Args:
        values (List[int]): List of salary values.

    Returns:
        float: The average value of the list.
    """
    return sum(values) / len(values) if values else 0.0


def group_salaries_by_company(
    data: List[Tuple[str, int]]
) -> Dict[str, List[int]]:
    """
    Groups employee salaries by company.

    Args:
        data (List[Tuple[str, int]]): A list of (company name, salary) pairs.

    Returns:
        Dict[str, List[int]]: A dictionary where keys are company names,
        and values are lists of salaries.
    """
    company_salaries = defaultdict(list)

    for company, salary in data:
        company_salaries[company].append(salary)

    return company_salaries


def compute_average_salaries(
    salaries_per_company: Dict[str, List[int]]
) -> Dict[str, float]:
    """
    Computes average salary for each company.

    Args:
        salaries_per_company (Dict[str, List[int]]): A dictionary of company
        names and salaries.

    Returns:
        Dict[str, float]: A dictionary of company names and their average
        salaries.
    """
    return {
        company: compute_average_value(salaries)
        for company, salaries in salaries_per_company.items()
    }


def sort_companies_by_avg_salary(
    data: List[Tuple[str, int]]
) -> List[Tuple[str, float]]:
    """
    Sorts companies by their average salary in ascending order.
    If two companies have the same average salary, they are sorted
    alphabetically.

    Args:
        data (List[Tuple[str, int]]): A list of (company name, salary) pairs.

    Returns:
        List[Tuple[str, float]]: A sorted list of (company name, average
        salary) pairs.
    """
    salaries_per_company = group_salaries_by_company(data)
    average_salaries = compute_average_salaries(salaries_per_company)
    return sorted(
        average_salaries.items(), key=lambda item: (item[1], item[0])
    )


def display_sorted_companies(sorted_data: List[Tuple[str, float]]) -> None:
    """
    Prints sorted company names.

    Args:
        sorted_data (List[Tuple[str, float]]): A list of (company name,
        average salary) pairs.
    """
    for company_name, _ in sorted_data:
        print(company_name)


filename = 'salary_data.csv'
data = read_csv_data(filename)
sorted_companies = sort_companies_by_avg_salary(data)
display_sorted_companies(sorted_companies)

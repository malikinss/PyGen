'''
TODO:
        You have access to the students.json file, which contains a list of
        JSON objects that represent data about students in a particular course:
            [
                {
                    "name": "Holly-Anne",
                    "city": "Abilene",
                    "age": 29,
                    "progress": 85,
                    "phone": "(802) 983-9126"
                },
                ...
            ]

        By "student" we mean one JSON object from this list.

        A student has the following attributes:
            name — name
            city — city of residence
            age — age
            progress — progress in the course in percentage
            phone — contact number

        Write a program that identifies students who meet the following
        conditions:
            age 18 or older
            progress in the course 75% or more

        The program should create a data.csv file with two columns — name and
        phone, and write the data of the selected students to it, arranging
        them in lexicographic order of names.

        A comma should be used as a separator in the data.csv file.

NOTE:
        It is guaranteed that all students have different names.

        The initial part of the data.csv file looks like this:
            name,phone
            Cary,(580) 476-8517
            Catarina,(237) 608-2757
            Catherin,(876) 215-3666
            ...
'''
import json
import csv
from typing import Dict, List


def read_json_file(file_path: str) -> List[Dict[str, str]]:
    """
    Read JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict[str, str]]: List of dictionaries containing JSON data.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not valid JSON.")
        return []


def write_csv(
    data: List[Dict[str, str]],
    filename: str,
    columns: List[str],
    delimiter: str = ','
) -> None:
    """
    Writes data to a CSV file.

    Args:
        data: The data to write, as a list of dictionaries.
        filename: The path to the output CSV file.
        columns: The column names to use in the CSV file.
        delimiter: The delimiter to use in the CSV file.
    """
    try:
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file,
                                    fieldnames=columns,
                                    delimiter=delimiter)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Error writing to file {filename}: {e}")


def is_eligible_student(student: Dict[str, str]) -> bool:
    """
    Check if a student is eligible based on age and progress criteria.

    Args:
        student (Dict[str, str]): Dictionary representing a student.

    Returns:
        bool: True if the student is eligible, False otherwise.
    """
    try:
        age = int(student['age'])
        progress = float(student['progress'])
    except (ValueError, KeyError):
        return False

    return age >= 18 and progress >= 75


def filter_students_by_criteria(
    students_data: List[Dict[str, str]]
) -> List[Dict[str, str]]:
    """
    Filters students based on age and progress criteria.

    Args:
        students_data (List[Dict[str, str]]): List of student dictionaries.

    Returns:
        List[Dict[str, str]]: List of filtered student dictionaries.
    """
    eligible_students = [
        {'name': student['name'], 'phone': student['phone']}
        for student in students_data
        if is_eligible_student(student)
    ]

    return sorted(eligible_students, key=lambda x: x['name'])


def process_student_data(input_file_path: str, output_file_path: str) -> None:
    """
    Process the student data from the JSON file, filter eligible students,
    and write to a CSV file.

    Args:
        input_file_path (str): Path to the input JSON file.
        output_file_path (str): Path to the output CSV file.
    """
    data = read_json_file(input_file_path)

    if data:
        students = filter_students_by_criteria(data)
        if students:
            headers = list(students[0].keys())
            write_csv(students, output_file_path, headers)
        else:
            print("No students met the eligibility criteria.")
    else:
        print("No data to process.")


# Example usage
input_file_path = 'students.json'
output_file_path = 'data.csv'
process_student_data(input_file_path, output_file_path)

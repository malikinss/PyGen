'''
TODO:
        You have access to the exam_results.csv file, which contains
        information about a past exam at a certain educational institution.

        The first column contains the student's name;
        The second column contains the last name;
        The third column contains the exam grade;
        The fourth column contains the date and time of the exam
        in the next format:
            YYYY-MM-DD HH:MM:SS
        The fifth column contains the email address:
            name,surname,score,date_and_time,email
            Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
            April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
            ...

        Each student has the right to retake the exam twice, so it can appear
        in the original file up to three times with different grades and
        different dates and times of the exam.

        Write a program that determines the best grade for each student, as
        well as the date and time it was received.

        The program should create a list of dictionaries, each containing the
        following key-value pairs:
            name — student's first name
            surname — student's last name
            best_score — best grade for the exam
            date_and_time — date and time of receiving the best grade in
                            the original format
            email — email address

        The program should write the resulting list to the best_scores.json
        file, and the dictionaries in the list should be arranged in
        lexicographic order of email names.

NOTE:
        If the student received the same grade on the retake as the previous
        time, then the date should be specified as the retake date.

        A comma is used as a separator in the exam_results.csv file, and
        quotation marks are not used.

        The initial part of the best_scores.json file looks like this:
            [
                {
                    "name": "Stephen",
                    "surname": "Farley",
                    "best_score": 3,
                    "date_and_time": "2021-11-12 12:00:00",
                    "email": "aardo@mac.com"
                },
                {
                    "name": "Kaylen",
                    "surname": "Horne",
                    "best_score": 4,
                    "date_and_time": "2021-11-09 11:00:00",
                    "email": "aaribaud@att.net"
                },
                ...
            ]
'''
import json
import csv
from typing import Dict, List, Union
from datetime import datetime


DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def read_csv(filename: str, delimiter: str = ',') -> List[Dict[str, str]]:
    """Read and parse CSV file with exam results.

    Args:
        filename (str): Path to the CSV file.
        delimiter (str): Delimiter used in the CSV file.

    Returns:
        List[Dict[str, str]]: List of dictionaries containing exam records.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        return list(reader)


def write_json_file(
    data: List[Dict[str, Union[str, int]]],
    file_path: str
) -> None:
    """
    Write processed exam results to JSON file.

    Args:
        data (List[Dict[str, Union[str, int]]]): Processed exam results.
        file_path (str): Path to the output JSON file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_student_records(
    records: List[Dict[str, str]],
    name: str,
    surname: str
) -> List[Dict[str, str]]:
    """
    Get all exam records for a specific student.

    Args:
        records (List[Dict[str, str]]): List of all exam records.
        name (str): Student's first name.
        surname (str): Student's last name.

    Returns:
        List[Dict[str, str]]: List of student's exam records.
    """
    return [
        record for record in records
        if record['name'] == name and record['surname'] == surname
    ]


def create_grade_record(
    student_info: Dict[str, str],
    best_score: int
) -> Dict[str, Union[str, int]]:
    """
    Create a formatted grade record with the best score.

    Args:
        student_info (Dict[str, str]): Student's exam record.
        best_score (int): Student's best score.

    Returns:
        Dict[str, Union[str, int]]: Formatted grade record.
    """
    return {
        'name': student_info['name'],
        'surname': student_info['surname'],
        'best_score': best_score,
        'date_and_time': student_info['date_and_time'],
        'email': student_info['email']
    }


def find_records_with_best_grade(
    records: List[Dict[str, str]]
) -> List[Dict[str, Union[str, int]]]:
    """
    Find all records with the highest grade.

    Args:
        records (List[Dict[str, str]]): List of student's exam records.

    Returns:
        List[Dict[str, Union[str, int]]]: Records with the highest grade.
    """
    best_grade = max(int(record['score']) for record in records)
    return [
        create_grade_record(record, best_grade)
        for record in records
        if int(record['score']) == best_grade
    ]


def get_latest_record(
    records: List[Dict[str, Union[str, int]]]
) -> Dict[str, Union[str, int]]:
    """
    Get the record with the most recent date.

    Args:
        records (List[Dict[str, Union[str, int]]]): List of exam records.

    Returns:
        Dict[str, Union[str, int]]: Most recent exam record.
    """
    return max(
        records,
        key=lambda x: datetime.strptime(
            str(x['date_and_time']), DATETIME_FORMAT
        )
    )


def get_best_grade_record(
    records: List[Dict[str, str]]
) -> Dict[str, Union[str, int]]:
    """
    Get student's best grade record considering date and time.

    Args:
        records (List[Dict[str, str]]): List of student's exam records.

    Returns:
        Dict[str, Union[str, int]]: Best grade record with latest date.
    """
    best_grade_records = find_records_with_best_grade(records)
    return (
        get_latest_record(best_grade_records)
        if len(best_grade_records) > 1
        else best_grade_records[0]
    )


def is_person_exists(
    records: List[Dict[str, Union[str, int]]],
    name: str,
    surname: str
) -> bool:
    """
    Check if person already exists in processed records.

    Args:
        records (List[Dict[str, Union[str, int]]]): Processed records.
        name (str): Student's first name.
        surname (str): Student's last name.

    Returns:
        bool: True if person exists, False otherwise.
    """
    return any(
        record['name'] == name and record['surname'] == surname
        for record in records
    )


def get_best_grades(
    records: List[Dict[str, str]]
) -> List[Dict[str, Union[str, int]]]:
    """
    Process exam records and get best grades for all students.

    Args:
        records (List[Dict[str, str]]): List of all exam records.

    Returns:
        List[Dict[str, Union[str, int]]]: Best grades sorted by email.
    """
    best_grades_list: List = []

    for record in records:
        name, surname = record['name'], record['surname']

        if not is_person_exists(best_grades_list, name, surname):
            student_records = get_student_records(records, name, surname)
            best_record = get_best_grade_record(student_records)
            best_grades_list.append(best_record)

    return sorted(best_grades_list, key=lambda x: x['email'])


def process_exam_results(input_path: str, output_path: str) -> None:
    """
    Process exam results and save best grades to JSON file.

    Args:
        input_path (str): Path to input CSV file.
        output_path (str): Path to output JSON file.
    """
    exam_results = read_csv(input_path)
    best_grades = get_best_grades(exam_results)
    write_json_file(best_grades, output_path)


process_exam_results('exam_results.csv', 'best_scores.json')

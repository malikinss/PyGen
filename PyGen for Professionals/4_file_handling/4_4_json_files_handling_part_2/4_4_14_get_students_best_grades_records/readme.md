# Exam Results Processing 📊

## Description 📝

This program processes student exam results from a `CSV` file, extracts the best grades for each student, and saves the results in a `JSON` file.
Each student can have up to three exam records, and the program selects the best grade and the most recent date for each student.
The output is sorted by the student's email address.

## Purpose 🎯

The purpose of this project is to demonstrate how to process and manipulate data from `CSV` files, compute the best results for each student, and output the results in a structured `JSON` format.

## How It Works 🔍

1. The program reads the `exam_results.csv` file, which contains exam records for each student.
2. It processes the records, determining the best grade for each student based on the highest score and most recent date.
3. The program generates a list of dictionaries, each representing a student's best exam result, including their name, surname, best score, date of the exam, and email.
4. The resulting list is saved to `best_scores.json` and sorted by email.

## Output 📜

The output file, `best_scores.json`, will contain the following structure:

```json
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
    }
]
```

## Usage 📦

1. Prepare the `exam_results.csv` file containing the exam records.
2. Place the CSV file in the same directory as the Python script.
3. Run the script:
    ```bash
    python script_name.py
    ```
4. The program will generate the `best_scores.json` file in the same directory.

## Conclusion 🚀

This project demonstrates the ability to process, manipulate, and export structured data from `CSV` to `JSON` format, while ensuring the data is sorted by email and the best grades are selected for each student.

# Student Eligibility Filter Program 📝

## Description 📝

This program processes student data from a `students.json` file, filtering out students who meet specific eligibility criteria (age ≥ 18 and progress ≥ 75%).
The program creates a `data.csv` file containing the names and phone numbers of eligible students, sorted in lexicographic order by name.

## Purpose 🎯

The goal of this program is to generate a `CSV` file that lists the eligible students, based on age and course progress.
This can be useful for any application that needs to gather or report information about students who meet certain criteria.

## How It Works 🔍

1. **Read the Input Data**: The program starts by reading the student data from a JSON file (`students.json`).
2. **Filter Eligible Students**: It filters the students who are 18 years or older and have 75% or more progress in the course.
3. **Sort by Name**: The filtered students are sorted in lexicographic order by their name.
4. **Write to CSV**: The program writes the name and phone number of each eligible student to a CSV file (`data.csv`), using a comma as a separator.

### Key Details:

-   Input: A JSON file (`students.json`) with student data.
-   Output: A CSV file (`data.csv`) with the names and phone numbers of eligible students.

## Output 📜

### Example:

#### Input (`students.json`):

```json
[
    {
        "name": "Holly-Anne",
        "city": "Abilene",
        "age": 29,
        "progress": 85,
        "phone": "(802) 983-9126"
    },
    {
        "name": "Cary",
        "city": "Raleigh",
        "age": 22,
        "progress": 80,
        "phone": "(580) 476-8517"
    },
    {
        "name": "Catherin",
        "city": "Dallas",
        "age": 17,
        "progress": 90,
        "phone": "(876) 215-3666"
    }
]
```

#### Output (`data.csv`):

```csv
name,phone
Cary,(580) 476-8517
Holly-Anne,(802) 983-9126
```

## Usage 📦

1. Ensure that the `students.json` file is available and contains the student data.
2. Run the program. It will process the student data, filter based on the criteria, and generate the `data.csv` file.
3. The resulting `CSV` file will contain only eligible students, with names and phone numbers sorted lexicographically.

## Conclusion 🚀

This program provides a simple yet efficient way to filter and organize student data based on specific eligibility criteria, making it ideal for applications that require reports or lists of students who meet certain conditions.

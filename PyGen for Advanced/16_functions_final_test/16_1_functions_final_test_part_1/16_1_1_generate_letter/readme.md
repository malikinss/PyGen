# Exam Schedule Email Generator 📧

## Description 📝

This function generates an email text for exam scheduling based on the provided details.
It assembles the email according to the specified template, with options for default values for the teacher and room number.

## Purpose 🎯

The function `generate_letter()` creates a formatted email that informs a student about their upcoming exam.
It provides the necessary details such as the exam date, time, place, teacher, and room number.

## How It Works 🔍

-   The function takes five mandatory arguments: the student's email address, name, exam date, time, and place.
-   Two optional arguments allow customization of the teacher and room number.
    If these are not provided, the default values are used: teacher "Тимур Гуев" and room number "17".
-   The email is constructed with the provided details and returned as a string.

## Example Output:

```text
To: student@example.com
Hello, John!
You have an exam scheduled for 2025-02-10, at 10:00.
At: Room 301.
The exam will be conducted by Timur Guev in room 17.
Good luck on the exam!
```

## Usage 📦

1. Provide the recipient's email, name, exam date, time, and place.
2. Optionally, specify the teacher and room number.
3. The function returns the email text, which can be sent to the student.

## Conclusion 🚀

This function simplifies the process of sending exam details to students, ensuring that all necessary information is included and formatted correctly.

'''
TODO:
    Write a program that, given a course number, prints information about
    that course.

    Course num (key) - Room number (value) - Instructor (value) - Time (value)
        CS101        - 3004                - Hines              - 8:00
        CS102        - 4501                - Alvarado           - 9:00
        CS103        - 6755                - Rich               - 10:00
        NT110        - 1244                - Burke              - 11:00
        CM241        - 1411                - Lee                - 13:00

NOTE:
    Use a dictionary instead of a conditional statement.
    For neater output, use the string format() method or f-strings.
'''

COURSES = {
    'CS101': ['3004', 'Hines', '8:00'],
    'CS102': ['4501', 'Alvarado', '9:00'],
    'CS103': ['6755', 'Rich', '10:00'],
    'NT110': ['1244', 'Burke', '11:00'],
    'CM241': ['1411', 'Lee', '13:00']
}


def print_course_info(course_id: str) -> None:
    """
    Prints the details of the given course in a formatted manner.

    Arguments:
    course_id: str -- the course identifier (e.g., 'CS101')

    Returns:
    None
    """
    if course_id in COURSES:
        room, instructor, time = COURSES[course_id]
        print(f"{course_id}: {room}, {instructor}, {time}")
    else:
        print(f"Course {course_id} not found.")


# Get user input and display course info
course_id_input = input("Enter the course number: ")
print_course_info(course_id_input)

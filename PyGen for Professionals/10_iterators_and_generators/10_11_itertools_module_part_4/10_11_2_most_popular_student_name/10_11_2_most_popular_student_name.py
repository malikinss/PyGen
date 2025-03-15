'''
TODO:
    You have access to a named tuple Student, which contains data about
    a student.

    The first element of the named tuple is the student's last name, the
    second is the first name, and the third is the class.

    You also have access to a list students, which contains these tuples.

    Complete the code below to return the most common name among the students
    in the list.

NOTE:
    It is guaranteed that the name you are looking for is unique.
'''
from collections import namedtuple
from itertools import groupby
from typing import List

# Defining the Student namedtuple
Student = namedtuple('Student', ['surname', 'name', 'grade'])

# List of students
students = [
    Student('Гагиев', 'Александр', 10),
    Student('Дедedkaев', 'Илья', 11),
    Student('Кодзаев', 'Георгий', 10),
    Student('Набокова', 'Алиса', 11),
    Student('Кораев', 'Артур', 10),
    Student('Шилин', 'Александр', 11),
    Student('Уртаева', 'Илина', 11),
    Student('Салбиев', 'Максим', 10),
    Student('Капустин', 'Илья', 11),
    Student('Гудцев', 'Таймураз', 11),
    Student('Перчиков', 'Максим', 10),
    Student('Чен', 'Илья', 11),
    Student('Елькина', 'Мария', 11),
    Student('Макоев', 'Руслан', 11),
    Student('Албегов', 'Хетаг', 11),
    Student('Щербак', 'Илья', 10),
    Student('Идрисов', 'Баграт', 11),
    Student('Гапбаев', 'Герман', 10),
    Student('Цивинская', 'Анна', 10),
    Student('Туткевич', 'Юрий', 11),
    Student('Мусиков', 'Андраник', 11),
    Student('Гадзиев', 'Георгий', 11),
    Student('Белов', 'Юрий', 11),
    Student('Акоева', 'Диана', 11),
    Student('Денисов', 'Илья', 11),
    Student('Букулова', 'Диана', 10),
    Student('Акоева', 'Лера', 11)
]


def most_popular_student_name(students: List[Student]) -> str:
    """
    Finds and returns the most common first name among the students in
    the provided list.

    Args:
        students (List[Student]): A list of Student namedtuples containing
        information about students, including their surname, first name,
        and grade.

    Returns:
        str: The first name that appears most frequently among the students.

    Example:
        most_popular_student_name(students)
        # Output: 'Илья'
    """
    key_func: callable = lambda x: x.name

    students.sort(key=key_func)
    grouped = groupby(students, key=key_func)

    most_popular = max(
        ((name, len(list(group))) for name, group in grouped),
        key=lambda x: x[1]
    )

    print(most_popular[0])


most_popular_student_name(students)

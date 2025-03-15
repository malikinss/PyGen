'''
TODO:
    Every day Timur writes down the tasks he needs to complete in a notebook

    He breaks each task down into several actions.

    You can access the tasks list, which contains all of Timur's tasks.

    Each element of the list is a tuple of three elements:
        - the first is the task name
        - the second is the action
        - the third is the order.

    Complete the code below so that it displays all of Timur's tasks in
    alphabetical order, specifying for each a set of corresponding actions in
    the correct order, in the following format:
        <task>:
            1. <action>
            2. <action>
        ...

    There should be an empty line between the two tasks.

NOTE:
    The initial part of the answer looks like this (use four spaces as
    indents):
        USE Mathematics:
            1. complete the course on parameters

        Course on OOP:
            1. discuss the topics
            2. discuss the tasks
        ...
'''
from itertools import groupby
from typing import List, Tuple


INDENT = ' ' * 4

Task = Tuple[str, str, int]


def print_task(name: str, points: List[Task]) -> None:
    """
    Prints a task and its actions in the specified format.

    Args:
        name (str): The name of the task.
        points (List[Task]): The list of actions associated with the task.

    Returns:
        None
    """
    structured_points = ''
    for point in points:
        structured_points += f'{INDENT}{point[2]}. {point[1]}\n'

    print(f'{name}:\n{structured_points}')


def get_structured_tasks(tasks: List[Task]) -> None:
    """
    Groups tasks by their name and prints them in alphabetical order,
    with each task's actions listed in the correct order.

    Args:
        tasks (List[Task]): The list of tasks to be grouped and printed.

    Returns:
        None
    """
    key_func: callable = lambda x: x[0]
    tasks.sort(key=key_func)
    grouped = groupby(tasks, key=key_func)

    for task, group in grouped:
        print_task(task, sorted(group, key=lambda x: x[2]))


tasks = [
    ('Отдых', 'поспать днем', 3),
    ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
    ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
    ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
    ('Отдых', 'погулять вечером', 4),
    ('Курс по ооп', 'обсудить темы', 1),
    ('Урок по groupby', 'добавить задачи на программирование', 3),
    ('Урок по groupby', 'написать конспект', 1),
    ('Отдых', 'погулять днем', 2),
    ('Урок по groupby', 'добавить тестовые задачи', 2),
    ('Уборка', 'убраться в ванной', 2),
    ('Уборка', 'убраться в комнате', 1),
    ('Уборка', 'убраться на кухне', 3),
    ('Отдых', 'погулять утром', 1),
    ('Курс по ооп', 'обсудить задачи', 2)
]

get_structured_tasks(tasks)

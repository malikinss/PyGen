# `get_structured_tasks()` - Display Tasks and Actions

## Description 📝

The `get_structured_tasks()` function processes a list of tasks with their respective actions and orders, then displays them in alphabetical order of the task name.
Each task is listed with its corresponding actions, ordered by their respective sequence numbers.

## Purpose 🎯

✔ **Sorts tasks alphabetically** by name.  
✔ **Groups actions** by task, sorting actions by their order.  
✔ **Prints tasks and actions** in a formatted structure.

## How It Works 🔍

1. **Sort tasks alphabetically** by their name.
2. **Group tasks** by their name using `groupby()`.
3. **Sort actions** within each task by their sequence number.
4. **Print each task** with its corresponding actions in the required format.

## Usage 📦

```python
tasks_data = [
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

get_structured_tasks(tasks_data)
```

**Output:**

```plaintext
ЕГЭ Математика:
    1. доделать курс по параметрам

Курс по ооп:
    1. обсудить темы
    2. обсудить задачи

Отдых:
    1. погулять утром
    2. погулять днем
    3. поспать днем
    4. погулять вечером

Ответы на вопросы:
    1. ответить на вопросы в дискорде
    2. ответить на вопросы в курсах

Уборка:
    1. убраться в комнате
    2. убраться в ванной
    3. убраться на кухне

Урок по groupby:
    1. написать конспект
    2. добавить тестовые задачи
    3. добавить задачи на программирование
```

## Conclusion 🚀

This program groups and sorts tasks, displaying them in a readable format with their corresponding actions ordered correctly.
The output is well-organized, with clear indentation and separation between tasks.

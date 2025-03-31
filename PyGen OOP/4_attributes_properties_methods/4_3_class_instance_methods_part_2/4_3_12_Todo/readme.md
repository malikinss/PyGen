# Todo Class Task Manager

## Description 📝

The `Todo` class represents a to-do list where tasks are stored with associated priorities.
It starts empty and allows adding tasks as tuples of a task name and an integer priority.
The class provides methods to retrieve tasks by a specific priority, as well as the tasks with the lowest and highest priorities, maintaining their insertion order.

## Purpose 🎯

This class is designed to manage prioritized tasks, making it useful for personal organization tools, educational examples of list manipulation, or as a component in systems requiring priority-based task retrieval.

## How It Works 🔍

-   **Initialization**: The `__init__` method creates an empty list `things` to store task tuples.
-   **add() Method**: Adds a task as a `(name, priority)` tuple to the `things` list.
-   **get_by_priority() Method**: Filters tasks by a given priority `n` and returns their names in order.
-   **get_low_priority() Method**: Returns names of tasks with the minimum priority, or an empty list if none exist.
-   **get_high_priority() Method**: Returns names of tasks with the maximum priority, or an empty list if none exist.
-   **Helper Methods**: Internal methods extract priorities and filter tasks by priority.

## Output 📜

Example usage:

```python
todo = Todo()
todo.add("Write report", 2)
todo.add("Buy groceries", 1)
todo.add("Call mom", 2)
print(todo.get_by_priority(2))     # Output: ['Write report', 'Call mom']
print(todo.get_low_priority())     # Output: ['Buy groceries']
print(todo.get_high_priority())    # Output: ['Write report', 'Call mom']
```

## Usage 📦

1. Save the class in a Python file, e.g., `todo.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from todo import Todo
my_todo = Todo()
my_todo.add("Exercise", 3)
my_todo.add("Read book", 1)
my_todo.add("Meeting", 3)
print(f"Priority 3: {my_todo.get_by_priority(3)}")  # Output: Priority 3: ['Exercise', 'Meeting']
print(f"Low: {my_todo.get_low_priority()}")         # Output: Low: ['Read book']
print(f"High: {my_todo.get_high_priority()}")       # Output: High: ['Exercise', 'Meeting']
```

## Conclusion 🚀

The `Todo` class offers a practical and efficient way to manage a prioritized to-do list in Python.
Its ability to filter tasks by priority and identify extremes makes it a versatile tool for task organization, easily extensible with features like task removal or priority updates for more complex applications.

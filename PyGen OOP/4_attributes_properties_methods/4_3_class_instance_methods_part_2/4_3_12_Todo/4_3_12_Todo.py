'''
TODO:
    Implement a Todo class that describes a to-do list.

    The class should not take any arguments when instantiated.

    An instance of the Todo class must have one attribute:
        - things — an initially empty list of things to do

    The Todo class must have four instance methods:
        - add() — a method that takes a thing and its priority (an integer)
        and adds the thing to the todo list as a tuple:
            (<thing>, <priority>)
        - get_by_priority() — a method that takes an integer n as an argument
        and returns a list of things with priority n
        - get_low_priority() — a method that returns a list of things with the
        lowest priority
        - get_high_priority() — a method that returns a list of things with
        the highest priority

NOTE:
    The things in the lists returned by get_by_priority(), get_low_priority(),
    and get_high_priority() must be in the order in which they were added
    to the list.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with valid data.
'''
from typing import List, Tuple


class Todo:
    """
    A class representing a to-do list with prioritized tasks.

    This class maintains a list of tasks, each stored as a tuple of a task
    name and its priority.

    It provides methods to add tasks and retrieve them by priority levels.

    Attributes:
        things (list[tuple[str, int]]): A list of tasks as (name, priority)
        tuples.

    Methods:
        add(name, priority): Adds a task with its priority to the list.
        get_by_priority(n): Returns a list of tasks with the specified
        priority.
        get_low_priority(): Returns a list of tasks with the lowest priority.
        get_high_priority(): Returns a list of tasks with the highest priority.
    """

    def __init__(self) -> None:
        """
        Initialize a Todo instance with an empty task list.

        Sets up the to-do list as an empty list of tasks.

        Returns:
            None
        """
        self.things: List[Tuple[str, int]] = []

    def add(self, name: str, priority: int) -> None:
        """
        Add a task with its priority to the to-do list.

        Appends a tuple of the task name and its priority to the list.

        Args:
            name (str): The name of the task to add.
            priority (int): The priority of the task.

        Returns:
            None
        """
        self.things.append((name, priority))

    def _get_priorities(self) -> List[int]:
        """
        Return a list of priorities of all tasks.

        Extracts the priority from each task tuple in the list.

        Returns:
            list[int]: A list of task priorities.
        """
        return [thing[1] for thing in self.things]

    def _filter_by_priority(self, priority: int) -> List[str]:
        """
        Return a list of task names with the specified priority.

        Filters tasks by the given priority, returning their names in order.

        Args:
            priority (int): The priority to filter by.

        Returns:
            list[str]: A list of task names with the specified priority.
        """
        return [thing[0] for thing in self.things if thing[1] == priority]

    def get_by_priority(self, n: int) -> List[str]:
        """
        Return a list of tasks with the specified priority.

        Retrieves all task names with the given priority in their original
        order.

        Args:
            n (int): The priority to filter by.

        Returns:
            list[str]: A list of task names with priority n.
        """
        return self._filter_by_priority(n)

    def get_low_priority(self) -> List[str]:
        """
        Return a list of tasks with the lowest priority.

        Retrieves all task names with the minimum priority in their original
        order.

        Returns an empty list if the to-do list is empty.

        Returns:
            list[str]: A list of task names with the lowest priority.
        """
        if not self.things:
            return []
        low_priority = min(self._get_priorities())
        return self._filter_by_priority(low_priority)

    def get_high_priority(self) -> List[str]:
        """
        Return a list of tasks with the highest priority.

        Retrieves all task names with the maximum priority in their original
        order.

        Returns an empty list if the to-do list is empty.

        Returns:
            list[str]: A list of task names with the highest priority.
        """
        if not self.things:
            return []
        high_priority = max(self._get_priorities())
        return self._filter_by_priority(high_priority)

'''
TODO:
    Implement a class called DevelopmentTeam that describes a team of
    developers at two levels: junior and senior.

    The class should not take any arguments when instantiated.

    The DevelopmentTeam class should have two instance methods:
        - add_junior() — a method that takes an arbitrary number of positional
                         arguments, each of which is a developer name, and
                         adds them to the number of junior developers
        - add_senior() — a method that takes an arbitrary number of positional
                         arguments, each of which is a developer name, and
                         adds them to the number of senior developers

    An instance of the DevelopmentTeam class should be an iterable whose
    elements are first all its junior developers, and then all its senior
    developers.

    Junior developers should be represented as tuples:
        (<developer name>, 'junior')
    while senior developers should be represented as tuples:
        (<developer name>, 'senior')

NOTE:
    Developers in teams should be listed in the order they were added.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the DevelopmentTeam class, it can be arbitrary.
'''
from typing import Any, Iterable


class DevelopmentTeam:
    """
    A class representing a team of junior and senior developers.

    Instances are iterable, yielding tuples of (name, 'junior') for junior
    developers followed by (name, 'senior') for senior developers, in
    the order they were added.
    """

    def __init__(self) -> None:
        """
        Initialize an empty DevelopmentTeam.
        """
        self._juniors = []
        self._seniors = []

    def add_junior(self, *names: Any) -> None:
        """
        Add junior developers to the team.

        Args:
            *names: Names of junior developers to add.
        """
        self._juniors.extend(names)

    def add_senior(self, *names: Any) -> None:
        """
        Add senior developers to the team.

        Args:
            *names: Names of senior developers to add.
        """
        self._seniors.extend(names)

    def __iter__(self) -> Iterable[tuple[Any, str]]:
        """
        Return an iterator over developers.

        Returns:
            Iterable: Yields tuples (name, 'junior') for juniors,
                      then (name, 'senior') for seniors, in the order they
                      were added.
        """
        for name in self._juniors:
            yield (name, 'junior')
        for name in self._seniors:
            yield (name, 'senior')

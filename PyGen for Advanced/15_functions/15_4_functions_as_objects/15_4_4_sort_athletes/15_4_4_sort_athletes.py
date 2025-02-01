'''
TODO:
    The list athletes contains information about athletes in the form of
    tuples: (name, age, height, weight).

    Write a program to sort the list of athletes by the specified field:
        1: by name;
        2: by age;
        3: by height;
        4: by weight.

NOTE:
    Solve the problem without using the conditional operator.
'''
from typing import List, Tuple, Union, Callable


def sort_by_name(sequence: Tuple[str, int, int, int]) -> str:
    """
    Returns the name of the athlete for sorting.

    Args:
        sequence (Tuple[str, int, int, int]): Athlete's information as a tuple.

    Returns:
        str: Name of the athlete.
    """
    return sequence[0]


def sort_by_age(sequence: Tuple[str, int, int, int]) -> int:
    """
    Returns the age of the athlete for sorting.

    Args:
        sequence (Tuple[str, int, int, int]): Athlete's information as a tuple.

    Returns:
        int: Age of the athlete.
    """
    return sequence[1]


def sort_by_height(sequence: Tuple[str, int, int, int]) -> int:
    """
    Returns the height of the athlete for sorting.

    Args:
        sequence (Tuple[str, int, int, int]): Athlete's information as a tuple.

    Returns:
        int: Height of the athlete.
    """
    return sequence[2]


def sort_by_weight(sequence: Tuple[str, int, int, int]) -> int:
    """
    Returns the weight of the athlete for sorting.

    Args:
        sequence (Tuple[str, int, int, int]): Athlete's information as a tuple.

    Returns:
        int: Weight of the athlete.
    """
    return sequence[3]


def sort_athletes(
    athletes: List[Tuple[str, int, int, int]],
    sort_func: Callable[[Tuple[str, int, int, int]], Union[int, str]]
) -> None:
    """
    Sorts the list of athletes according to a given sorting function and
    prints the sorted list.

    Args:
        athletes (List[Tuple[str, int, int, int]]): List of athletes
                                                    represented by tuples.
        sort_func (Callable[[Tuple[str, int, int, int]], Union[int, str]]):
            Function to use for sorting.
    """
    for athlete in sorted(athletes, key=sort_func):
        print(*athlete)


# Dictionary to map input choices to sort functions
my_sort_funcs: dict[str, Callable[[Tuple[str, int, int, int]], int | str]] = {
    '1': sort_by_name,
    '2': sort_by_age,
    '3': sort_by_height,
    '4': sort_by_weight
}

# Athlete list
athletes: List[Tuple[str, int, int, int]] = [
    ('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33),
    ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
    ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)
]

# Taking the user's choice for sorting
chosen_sort: str = input(
    "Enter the number to sort by (1: Name, 2: Age, 3: Height, 4: Weight): "
)

# Sorting athletes by the chosen attribute and printing the sorted list
sort_athletes(athletes, my_sort_funcs[chosen_sort])

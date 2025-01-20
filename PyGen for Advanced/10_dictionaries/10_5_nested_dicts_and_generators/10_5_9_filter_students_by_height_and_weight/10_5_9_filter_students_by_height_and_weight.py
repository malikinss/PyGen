'''
TODO:
    The variable students stores a dictionary containing information about the
    height (in cm) and weight (in kg) of students.

    Complete the code given using the generator so that you get a dictionary
    result consisting of all elements of the dictionary students where the
    height is greater than 167 cm and the weight is less than 75 kg.

NOTE:
    There is no need to output the contents of the dictionary result.
'''
from typing import Dict, Tuple


def filter_students_by_height_and_weight(
    students: Dict[str, Tuple[int, int]]
) -> Dict[str, Tuple[int, int]]:
    """
    This function filters the `students` dictionary to return a new dictionary
    containing only those students whose height is greater than 167 cm and
    weight is less than 75 kg.

    Args:
        students (Dict[str, Tuple[int, int]]): A dictionary where keys are
                                               student names (str), and values
                                               are tuples containing height
                                               (int) and weight (int).

    Returns:
        Dict[str, Tuple[int, int]]: A dictionary containing only students who
                                    meet the height and weight criteria.
    """
    # Using a generator within the dictionary comprehension
    return {
        key: value
        for key, value in students.items()
        if value[0] > 167 and value[1] < 75
    }


# Dictionary of students with their height (cm) and weight (kg)
students = {
    'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68),
    'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70),
    'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67),
    'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120),
    'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
    'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80),
    'Mary': (175, 69), 'Jane': (190, 80)
}

# Calling the function and storing the result
result = filter_students_by_height_and_weight(students)

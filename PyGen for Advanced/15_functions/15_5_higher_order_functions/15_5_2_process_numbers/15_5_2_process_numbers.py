'''
TODO:
    Write a program that uses the functions filter() and map() to select from
    a given list of numbers three-digit numbers that give a remainder
    of 2 when divided by 5, and output their cubes, each on a separate line.

NOTE:
    The remainder of 2 when divided by 5 should be the number itself,
    not its cube.
'''


def cube(number: int) -> int:
    """
    Returns the cube of the given number.

    Args:
        number (int): The number to cube.

    Returns:
        int: The cube of the number.
    """
    return number ** 3


def predicate(number: int) -> bool:
    """
    Checks if the number is a three-digit number and gives a remainder of 2
    when divided by 5.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number satisfies both conditions, otherwise False.
    """
    return 100 <= number <= 999 and number % 5 == 2


def process_numbers(numbers: list) -> list:
    """
    Filters the numbers that are three-digit and give remainder 2 when divided
    by 5, and returns their cubes.

    Args:
        numbers (list): The list of numbers to process.

    Returns:
        list: A list of cubes of numbers that meet the criteria.
    """
    return list(map(cube, filter(predicate, numbers)))


# List of numbers to process
numbers = [
    1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434,
    696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776,
    657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207,
    266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144,
    1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928,
    1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278,
    166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282,
    336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456,
    1268, 1018, 1274, 387, 120, 340, 963, 832, 1127
]

# Process the numbers and print their cubes
print(*process_numbers(numbers), sep='\n')

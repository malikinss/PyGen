'''
TODO:
    The Voskhod satellite has a device for measuring solar activity.

    Every minute it transmits a positive integer to the observatory via
    a communication channel — the amount of solar radiation energy.

    To correctly analyze the results, there is no need to keep repeating data,
    so they must be deleted.

    Write a program that outputs the maximum number of satellite readings,
    deleting which will correctly analyze the result.
'''


def calculate_repeated_readings(data: list) -> int:
    """
    Calculates the maximum number of repeated readings in the given data.

    Args:
        data (list): A list of satellite readings.

    Returns:
        int: The maximum number of repeated readings.
    """
    data_set = set(data)  # Unique readings
    return len(data) - len(data_set)  # Total readings minus unique readings


# Input the satellite readings
given_string = input().split()

# Calculate and print the number of repeated readings
print(calculate_repeated_readings(given_string))

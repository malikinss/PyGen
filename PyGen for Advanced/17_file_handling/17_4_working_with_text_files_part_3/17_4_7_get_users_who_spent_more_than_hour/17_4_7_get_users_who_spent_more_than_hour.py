'''
TODO:
    A text file is available to you "logfile.txt " with information about the
    time the user logs in and out of the system.

    Each line of the file contains three values separated by commas and
    a space character:
        -user name
        -entry time
        -exit time

    where the time is indicated in 24 - hour format.

    Write a program that creates a file "output.txt " and outputs to it the
    names of all users (without changing the order) who have been online for
    at least an hour.

NOTE:
    Assume that the executable program and the specified file are in the same
    folder.

    Consider that each user has been in the system only once, that is, there
    are no two lines in the file with the same user.
'''


def read_data_from_file(file_name: str) -> list:
    """
    Reads the content of a file and returns its lines without trailing newline
    characters.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        list: A list of lines from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as file:
        return [line.rstrip() for line in file.readlines()]


def write_data_to_file(file_name: str, data: list) -> None:
    """
    Writes a list of strings to a file.

    Args:
        file_name (str): The name of the file to write to.
        data (list): The list of strings to write to the file.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(data)


def convert_row_to_list(row: str) -> list:
    """
    Converts a comma-separated string row into a list.

    Args:
        row (str): A string representing one line of the file.

    Returns:
        list: A list of elements extracted from the string.
    """
    return row.split(', ')


def convert_str_time_to_int_min(time: str) -> int:
    """
    Converts a time in "HH:MM" format into minutes.

    Args:
        time (str): The time string in "HH:MM" format.

    Returns:
        int: The total time in minutes.
    """
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes


def get_minutes_difference(start_time: str, end_time: str) -> int:
    """
    Calculates the difference in minutes between two times.

    Args:
        start_time (str): The start time in "HH:MM" format.
        end_time (str): The end time in "HH:MM" format.

    Returns:
        int: The difference in minutes between the two times.
    """
    start_minutes = convert_str_time_to_int_min(start_time)
    end_minutes = convert_str_time_to_int_min(end_time)

    return end_minutes - start_minutes


def get_users_who_spent_more_than_hour(data: list) -> list:
    """
    Filters out users who have been online for at least one hour.

    Args:
        data (list): A list of data where each entry is
                     [user_name, entry_time, exit_time].

    Returns:
        list: A list of users who spent at least one hour online.
    """
    return [
        user
        for user, entry_time, exit_time in data
        if get_minutes_difference(entry_time, exit_time) >= 60
    ]


# Main logic to read the file, process the data, and write the results
readen_data = read_data_from_file('logfile.txt')
processed_data = [convert_row_to_list(row) for row in readen_data]
result_data_to_write = get_users_who_spent_more_than_hour(processed_data)

# Writing directly to the file with '\n' after each user
data = [user + '\n' for user in result_data_to_write]
write_data_to_file('output.txt', data)

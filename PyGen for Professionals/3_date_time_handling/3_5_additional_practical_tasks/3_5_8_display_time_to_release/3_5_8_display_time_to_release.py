'''
TODO:
    The BEEGEEK team plans to release their new course on 08.11.2022 at
    exactly 12:00.

    Write a program that takes the current date and time as input and
    determines how much time is left until the course is released.

    The program input is the current date and time in the format
        'DD.MM.YYYY HH:MM'

    The program should output text indicating the number of days and hours
    remaining until the course is released, in the following format:
        'There are: <number of days> days and <number of hours> hours left
        until the course is released'

    If in this case the number of hours is zero, then only days need to
    be displayed.

    If the number of days is zero, then you only need to display the hours and
    minutes in the following format:
        'There are: <number of hours> hours and <number of minutes> minutes
        left until the course is released'

    If in this case the number of minutes is zero, then only the hours need
    to be displayed.

    Similarly, if the number of hours is zero, then only minutes need
    to be output.

    If the entered date and time is greater than or equal to 08.11.2021 12:00,
    the program should output the text:
        'The course is out now!'
'''
from datetime import datetime


TIME_FORMAT = '%H:%M'
DATE_FORMAT = '%d.%m.%Y'

UNIT_PLURALS = {
    'd': ('day', 'days'),
    'h': ('hour', 'hours'),
    'm': ('minute', 'minutes')
}


def get_msg(time: str) -> str:
    """
    Returns the message indicating the time left until the course is released.

    Args:
        answer (time): The formatted string representing the remaining time.

    Returns:
        str: The full message with the time left until the course release.
    """
    return f'There are: {time} left until the course is released'


def parse_datetime(datetime_string: str) -> datetime:
    """
    Parses a datetime string into a datetime object.

    Args:
        datetime_string (str): The datetime string to parse in the format
                                'DD.MM.YYYY HH:MM'.

    Returns:
        datetime: The parsed datetime object.

    Raises:
        ValueError: If the datetime string doesn't match the expected format.
    """
    try:
        return datetime.strptime(
            datetime_string, f'{DATE_FORMAT} {TIME_FORMAT}'
        )
    except ValueError:
        raise ValueError(
            'Invalid datetime format. Please use the format DD.MM.YYYY HH:MM'
        )


def get_plural_form(amount: int, variants: tuple) -> str:
    """
    Returns the correct plural form based on the amount.

    Args:
        amount (int): The quantity to determine the plural form for.
        variants (tuple): A tuple containing the singular, genitive singular,
                          and plural forms of the word.

    Returns:
        str: The formatted string with the correct plural form based on
             the amount.
    """
    if amount == 1:
        return f'{amount} {variants[0]}'
    elif 2 <= amount <= 4:
        return f'{amount} {variants[1]}'
    else:
        return f'{amount} {variants[2]}'


def get_expanded_answer(answer: str, part_to_expand: str) -> str:
    """
    Combines the answer with an additional part.

    Args:
        answer (str): The initial part of the answer.
        part_to_expand (str): The part to add to the answer.

    Returns:
        str: The combined answer.
    """
    return f'{answer} and {part_to_expand}'


def get_answer_if_remain_more_than_day(
    remain_days: int, remain_hours: int
) -> str:
    """
    Returns the formatted answer when the remaining time is more than one day.

    Args:
        remain_days (int): The number of remaining days.
        remain_hours (int): The number of remaining hours.

    Returns:
        str: The formatted string with days and hours, if applicable.
    """
    result = get_plural_form(remain_days, UNIT_PLURALS['d'])
    if remain_hours > 0:
        part_to_expand = get_plural_form(remain_hours, UNIT_PLURALS['h'])
        result = get_expanded_answer(result, part_to_expand)
    return result


def get_answer_if_remain_less_than_day(
    remain_hours: int, remain_minutes: int
) -> str:
    """
    Returns the formatted answer when the remaining time is less than one day.

    Args:
        remain_hours (int): The number of remaining hours.
        remain_minutes (int): The number of remaining minutes.

    Returns:
        str: The formatted string with hours and minutes, if applicable.
    """
    result = get_plural_form(remain_hours, UNIT_PLURALS['h'])
    if remain_minutes > 0:
        part_to_expand = get_plural_form(remain_minutes, UNIT_PLURALS['m'])
        result = get_expanded_answer(result, part_to_expand)
    return result


def get_remaining_time(current_time: datetime, target_time: datetime) -> dict:
    """
    Calculates the remaining time between two datetimes.

    Args:
        current_time (datetime): The current datetime.
        target_time (datetime): The target datetime to compare with.

    Returns:
        dict: A dictionary with keys 'days', 'hours', and 'minutes'
              representing the remaining time.
    """
    delta = target_time - current_time
    return {
        'days': delta.days,
        'hours': delta.seconds // 3600,
        'minutes': (delta.seconds // 60) % 60
    }


def get_answer_for_remaining_time(remaining_time: dict) -> str:
    """
    Returns the appropriate answer based on the remaining time in days, hours,
    and minutes.

    Args:
        remaining_time (dict): A dictionary containing 'days', 'hours',
                               and 'minutes'.

    Returns:
        str: The formatted answer indicating the remaining time.
    """
    if remaining_time['days'] > 0:
        return get_answer_if_remain_more_than_day(
            remaining_time["days"], remaining_time["hours"]
        )
    elif remaining_time['hours'] > 0:
        return get_answer_if_remain_less_than_day(
            remaining_time["hours"], remaining_time["minutes"]
        )
    else:
        return get_plural_form(
            remaining_time["minutes"], UNIT_PLURALS["m"]
        )


def display_time_to_release() -> None:
    """
    Displays the remaining time until the course is released, based on
    the current date and time input by the user.

    If the current time is after the release time, it displays that the course
    is already released.
    """
    current_datetime = parse_datetime(input())
    release_datetime = datetime(2022, 11, 8, 12)

    if current_datetime < release_datetime:
        remaining_time = get_remaining_time(current_datetime, release_datetime)
        print(get_msg(get_answer_for_remaining_time(remaining_time)))
    else:
        print('The course is out now!')


display_time_to_release()

'''
TODO:
    Complete the code below to convert seconds (elapsed since the epoch) to
    a datetime object and, conversely, a datetime object to seconds
    (elapsed since the epoch).
'''
from datetime import datetime


def convert_seconds_to_datetime(seconds: int) -> datetime:
    """
    Converts seconds (elapsed since the epoch) to a datetime object.

    Args:
        seconds (int): The number of seconds since the epoch (January 1, 1970).

    Returns:
        datetime: The corresponding datetime object.
    """
    return datetime.fromtimestamp(seconds)


def convert_datetime_to_seconds(dt: datetime) -> int:
    """
    Converts a datetime object to seconds (elapsed since the epoch).

    Args:
        dt (datetime): The datetime object to convert.

    Returns:
        int: The number of seconds since the epoch.
    """
    return int(dt.timestamp())


# Example usage
seconds = 2483228800
dt = datetime(2011, 11, 4)

# Convert seconds to datetime
converted_dt = convert_seconds_to_datetime(seconds)
print("Converted datetime:", converted_dt)

# Convert datetime to seconds
converted_seconds = convert_datetime_to_seconds(dt)
print("Converted seconds:", converted_seconds)

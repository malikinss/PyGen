'''
TODO:
    Complete the code below so that the dt variable contains a datetime object
    with the date and time specified in the text string.

NOTE:
    The date specified in the text line is written in the DD.MM.YYYY format,
    and the time is in the HH:MM format.
'''
from datetime import datetime


def extract_datetime_from_text(text: str) -> datetime:
    """
    Extracts the date and time from a given text string and returns it as a
    datetime object.

    Args:
        text (str): The input text containing a date and time in the format
                    "DD.MM.YYYY" for the date and "HH:MM" for the time,
                    preceded by specific phrases.

    Returns:
        datetime: A datetime object representing the extracted date and time.
    """
    # Extract the relevant part of the text (the date and time part)
    dt_part = text.split(' on ')[1]
    dt_string = dt_part.split(' at ')[0] + ' ' + dt_part.split(' at ')[1]

    # Convert the extracted string to a datetime object
    return datetime.strptime(dt_string, '%d.%m.%Y %H:%M')


# Example usage
text = 'Dear patient, the doctor is ready to see you on 15.07.2022 at 08:30'
dt = extract_datetime_from_text(text)
print(dt)

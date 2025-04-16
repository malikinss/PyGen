'''
TODO:
    A log file is a text file that automatically records important information
    about the operation of a system or program.

    There are quite a few log file formats, but for the purposes of this task,
    we will assume that all log files have the following uniform format:
        2022-01-01 INFO: User logged in
        2022-01-01 ERROR: Invalid input data
        2022-01-01 WARNING: File not found
        2022-01-02 INFO: User logged out
        2022-01-03 INFO: User registered

    That is, each line of the log file describes a certain event, which
    is characterized by a date in the YYYY-MM-DD format, a type, and a brief
    description.

    Implement a log_for() function that takes two arguments in the following
    order:
        logfile — log file name
        date_str — string date in YYYY-MM-DD format

    The function should create a text file named:
        log_for_<date_str>.txt
    and write to it all events from the logfile file that occurred on date_str.

    The events should be written without a date, and also in their original
    order.

NOTE:
    The file name passed to the function already contains an extension.

    When opening the file, use an explicit UTF-8 encoding.
'''


def log_for(logfile: str, date_str: str) -> None:
    """
    Create a log file for events on a specific date.

    Args:
        logfile: Name of the input log file (with extension).
        date_str: Date in YYYY-MM-DD format.

    Creates:
        A file named log_for_<date_str>.txt containing events from logfile
        for the specified date, without the date prefix, in original order.
    """
    output_file = f'log_for_{date_str}.txt'
    with (
        open(logfile, 'r', encoding='utf-8') as input_log,
        open(output_file, 'w', encoding='utf-8') as output_log
    ):
        for line in input_log:
            if line.startswith(date_str):
                # Split on first space after date (10 chars + space)
                log_data = line[11:]
                output_log.write(log_data)

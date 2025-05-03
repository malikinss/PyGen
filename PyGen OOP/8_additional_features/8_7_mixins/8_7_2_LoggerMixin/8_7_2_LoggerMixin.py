'''
TODO:
    Implement the LoggerMixin class that adds logging functionality to classes.

    The LoggerMixin class must have one instance method:
        log() — a method that takes the logging level and message text
        as arguments and outputs event information in the following format:
            [<current date and time>] - <logging level> - <name of the class
            to which the logging functionality is added>: <message text>

    The current date and time must be represented in the DD.MM.YYYY HH:MM:SS
    format.

NOTE:
    The current date and time contained in the logging string output by
    the log() method may differ from the values presented in the test data.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the LoggerMixin
    class, it can be arbitrary.
'''
from datetime import datetime


class LoggerMixin:
    """
    A mixin class for logging with timestamp, level, and class name.
    """
    # Date and time format: DD.MM.YYYY HH:MM:SS
    DT_FORMAT: str = "%d.%m.%Y %H:%M:%S"

    def log(self, level: str, message: str) -> None:
        """
        Log a message with timestamp, level, and class name.

        Args:
            level: Logging level (e.g., INFO, ERROR).
            message: Message text to log.
        """
        print(
            f"[{datetime.now().strftime(self.DT_FORMAT)}] - "
            f"{level} - {self.__class__.__name__}: {message}"
        )

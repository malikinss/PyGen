'''
TODO:
    Implement the WeatherWarning class, which describes an object that warns
    of weather changes.

    The class should not take any arguments when instantiated.

    The WeatherWarning class should have three instance methods:
        rain() — a method that outputs the text:
            Heavy rains and thunderstorms are expected
        snow() — a method that outputs the text:
            Snow and strong winds are expected
        low_temperature() — a method that outputs the text:
            A sharp drop in temperature is expected

    Also implement the WeatherWarningWithDate class, a subclass
    of WeatherWarning, which describes an object that warns of weather changes
    with a date.

    The process of instantiating the WeatherWarningWithDate class should
    coincide with the process of instantiating the WeatherWarning class.

    The WeatherWarningWithDate class must have three instance methods:
        rain() — a method that takes a date (type date) as an argument and
        outputs the text:
            <date in DD.MM.YYYY format>
            Heavy rains and thunderstorms are expected
        snow() — a method that takes a date (type date) as an argument and
        outputs the text:
            <date in DD.MM.YYYY format>
            Snow and strong winds are expected
        low_temperature() — a method that takes a date (type date) as
        an argument and outputs the text:
            <date in DD.MM.YYYY format>
            A strong drop in temperature is expected

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of classes, it can
    be arbitrary.
'''
from datetime import date

DATE_FORMAT = "%d.%m.%Y"


class WeatherWarning:
    """
    Class representing a weather warning system.

    This class provides methods to issue warnings about various weather
    conditions.
    """

    def rain(self) -> None:
        """
        Print a warning about heavy rains and thunderstorms.
        """
        print("Heavy rains and thunderstorms are expected")

    def snow(self) -> None:
        """
        Print a warning about snow and strong winds.
        """
        print("Snow and strong winds are expected")

    def low_temperature(self) -> None:
        """
        Print a warning about a sharp drop in temperature.
        """
        print("A sharp drop in temperature is expected")


class WeatherWarningWithDate(WeatherWarning):
    """
    Class representing a weather warning system with date information.

    Inherits from WeatherWarning and adds date information to weather warnings.
    """

    def rain(self, date: date) -> None:
        """
        Print a warning about heavy rains with the specified date.

        Args:
            date: The date of the weather warning.
        """
        print(date.strftime(DATE_FORMAT))
        super().rain()

    def snow(self, date: date) -> None:
        """
        Print a warning about snow with the specified date.

        Args:
            date: The date of the weather warning.
        """
        print(date.strftime(DATE_FORMAT))
        super().snow()

    def low_temperature(self, date: date) -> None:
        """
        Print a warning about a temperature drop with the specified date.

        Args:
            date: The date of the weather warning.
        """
        print(date.strftime(DATE_FORMAT))
        super().low_temperature()

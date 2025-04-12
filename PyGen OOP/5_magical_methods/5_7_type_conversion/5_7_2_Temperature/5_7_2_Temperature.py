'''
TODO:
    Implement a Temperature class that describes temperature in degrees
    Celsius.

    When instantiated, the class must accept one argument:
        temperature — the temperature in degrees Celsius

    The Temperature class must have one instance method:
        to_fahrenheit() — a method that returns the temperature in Fahrenheit

    The Temperature class must have one class method:
        from_fahrenheit() — a method that takes the temperature in Fahrenheit
                            as an argument and returns an instance of
                            the Temperature class created based on the passed
                            temperature

    An instance of the Temperature class must have the following informal
    string representation:
        <temperature in degrees Celsius rounded to two decimal places>°C

    Also, an instance of the Temperature class must support casting to bool,
    int, and float types:
        - when cast to bool, the value of an instance of the Temperature class
          must be True if its temperature is above zero, or False otherwise
        - when cast to int, the value of an instance of the Temperature class
          must be its temperature as an integer with the leading dropped
          fractional part
        - when casting to float, the value of a Temperature class instance
          must be its temperature as a real number

NOTE:
    The formula for converting a temperature from Fahrenheit to Celsius is:
        tC = (5/9)*(tF-32)
    where tC is the temperature in degrees Celsius, tF is the temperature in
    degrees Fahrenheit.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Temperature
    class, it can be arbitrary.
'''
from typing import Union


class Temperature:
    """
    A class representing temperature in degrees Celsius.
    """

    def __init__(self, temperature: Union[int, float]) -> None:
        """
        Initialize Temperature with a value in degrees Celsius.

        Args:
            temperature (int | float): Temperature in degrees Celsius.
        """
        self.temperature = temperature

    def to_fahrenheit(self) -> float:
        """
        Convert the temperature to Fahrenheit.

        Returns:
            float: Temperature in degrees Fahrenheit.
        """
        return self.temperature * 9/5 + 32

    @classmethod
    def from_fahrenheit(
        cls, temperature_f: Union[int, float]
    ) -> 'Temperature':
        """
        Create a Temperature instance from a Fahrenheit value.

        Args:
            temperature_f (int | float): Temperature in degrees Fahrenheit.

        Returns:
            Temperature: A Temperature instance with the equivalent Celsius
                         value.
        """
        return cls((temperature_f - 32) * 5/9)

    def __str__(self) -> str:
        """
        Return informal string representation of the temperature.

        Returns:
            str: Temperature rounded to two decimal places with '°C'.
        """
        return f'{round(self.temperature, 2)}°C'

    def __bool__(self) -> bool:
        """
        Return True if temperature is above zero, False otherwise.

        Returns:
            bool: True if temperature > 0, False otherwise.
        """
        return self.temperature > 0

    def __int__(self) -> int:
        """
        Return the temperature as an integer.

        Returns:
            int: Temperature with fractional part discarded.
        """
        return int(self.temperature)

    def __float__(self) -> float:
        """
        Return the temperature as a float.

        Returns:
            float: Temperature as a real number.
        """
        return float(self.temperature)

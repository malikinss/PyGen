'''
TODO:
    Implement the Seasons class, which describes an enumeration with seasons.

    The enumeration must have four elements:
        WINTER — an element with the value 1
        SPRING — an element with the value 2
        SUMMER — an element with the value 3
        FALL — an element with the value 4

    The enumeration element must have one method:
        text_value() — a method that takes the country code en or ru as
                       an argument and returns the string value of the element
                       depending on the passed argument.

    For WINTER en and ru, the values are winter and winter, respectively,
    for SPRING — spring and spring, for SUMMER — summer and summer,
    for FALL — fall and autumn

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the Seasons class, it can be arbitrary.
'''
from enum import Enum


class Seasons(Enum):
    """
    Seasons enumeration.
    """
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, code: str) -> str:
        """
        Get season name by language.

        Args:
            code: Language code ('en' or 'ru').

        Returns:
            str: Season name (e.g., 'winter' or 'autumn').
        """
        ru_names = {
            "WINTER": "зима",
            "SPRING": "весна",
            "SUMMER": "лето",
            "FALL": "осень"
        }
        return ru_names[self.name] if code == "ru" else self.name.lower()

'''
TODO:
    A hexadecimal color value is often used to encode a color.

    It is written in the format #RRGGBB, where RR (red), GG (green),
    and BB (blue) are hexadecimal integers in the range [00; FF] (or [0; 255]
    in decimal) that indicate the intensity of the corresponding colors.

    For example, #0000FF represents pure blue, since the blue component has
    the highest value (FF) and the others are 00.

    Implement a Color class that describes a color.

    When instantiated, the class must accept one argument:
        - hexcode — the hexadecimal value of the color

    An instance of the Color class must have three attributes:
        - r — the intensity of the red component of the color as
              a decimal number
        - g — the intensity of the green component of the color as
              a decimal number
        - b — the intensity of the blue component of the color as
              a decimal number

    The Color class must have one property:
        - hexcode — a read-write property that returns the hexadecimal value
                    of the color

NOTE:
    When the hexadecimal value of the color changes, the values of the r, g,
    and b attributes must also change.

    It is guaranteed that only uppercase Latin letters are used to write
    hexadecimal numbers.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Color class,
    it can be arbitrary.
'''


class Color:
    """
    A class representing a color in hexadecimal format.

    Attributes:
        r (int): The intensity of the red component (0-255).
        g (int): The intensity of the green component (0-255).
        b (int): The intensity of the blue component (0-255).

    Properties:
        hexcode (str): A read-write property returning the hexadecimal color
        value in the format 'RRGGBB'.
    """

    def __init__(self, hexcode: str) -> None:
        """
        Initialize a Color instance with a hexadecimal color value.

        Args:
            hexcode (str): The hexadecimal color value in the format 'RRGGBB'
            or '#RRGGBB'.
        """
        if hexcode.startswith('#'):
            hexcode = hexcode[1:]
        self.r: int = self._get_dec(hexcode[:2])
        self.g: int = self._get_dec(hexcode[2:4])
        self.b: int = self._get_dec(hexcode[4:6])

    def _get_hex(self, num: int) -> str:
        """
        Convert a decimal number to a two-digit hexadecimal string.

        Args:
            num (int): The decimal number to convert (0-255).

        Returns:
            str: A two-digit hexadecimal string (e.g., 'FF').
        """
        return f"{num:0>2X}"

    def _get_dec(self, hex_str: str) -> int:
        """
        Convert a two-digit hexadecimal string to a decimal number.

        Args:
            hex_str (str): A two-digit hexadecimal string (e.g., 'FF').

        Returns:
            int: The decimal value (0-255).
        """
        return int(hex_str, 16)

    @property
    def hexcode(self) -> str:
        """
        Get the hexadecimal value of the color.

        Returns:
            str: The hexadecimal color value in the format 'RRGGBB'.
        """
        r_hex = self._get_hex(self.r)
        g_hex = self._get_hex(self.g)
        b_hex = self._get_hex(self.b)
        return f"{r_hex}{g_hex}{b_hex}"

    @hexcode.setter
    def hexcode(self, hexcode: str) -> None:
        """
        Set the hexadecimal value of the color and update r, g, b attributes.

        Args:
            hexcode (str): The new hexadecimal color value in the format
            'RRGGBB' or '#RRGGBB'.
        """
        if hexcode.startswith('#'):
            hexcode = hexcode[1:]
        self.r = self._get_dec(hexcode[:2])
        self.g = self._get_dec(hexcode[2:4])
        self.b = self._get_dec(hexcode[4:6])

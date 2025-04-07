'''
TODO:
    Implement a PhoneNumber class that describes a phone number.

    When instantiated, the class must accept one argument:
        - phone_number — a ten-digit phone number in one of the following
                         formats:
                            1) dddddddddd
                            2) ddd ddd dddd

    An instance of the PhoneNumber class must have the following formal string
    representation:
        PhoneNumber('<phone number in dddddddddd format>')

    And the following informal string representation:
        <phone number in (ddd) ddd-dddd format>

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions on the implementation of the PhoneNumber class,
    it can be arbitrary.
'''


class PhoneNumber:
    """
    A class representing a ten-digit phone number.
    """

    def __init__(self, phone_number: str) -> None:
        """
        Initialize a PhoneNumber instance.

        Args:
            phone_number (str): A ten-digit phone number in 'dddddddddd' or
                                'ddd ddd dddd' format.
        """
        self.phone_number = phone_number.replace(" ", "")

    def __repr__(self) -> str:
        """
        Return a formal string representation of the phone number.

        Returns:
            str: The phone number in format "PhoneNumber('<dddddddddd>')".
        """
        return f"PhoneNumber('{self.phone_number}')"

    def __str__(self) -> str:
        """
        Return an informal string representation of the phone number.

        Returns:
            str: The phone number in format '(ddd) ddd-dddd'.
        """
        region = self.phone_number[:3]
        first_three = self.phone_number[3:6]
        last_four = self.phone_number[6:]
        return f"({region}) {first_three}-{last_four}"

'''
TODO:
    HTTP status codes are three-digit integers and are used to indicate
    the success of a particular HTTP request.

    There are five groups of status codes:
        information (100-199)
        success (200-299)
        redirect (300-399)
        client error (400-499)
        server error (500-599)

    Implement the HTTPStatusCodes class, which describes an enumeration with
    HTTP status codes.

    The enumeration must have five elements:
        CONTINUE — element with value 100
        OK — element with value 200
        USE_PROXY — element with value 305
        NOT_FOUND — element with value 404
        BAD_GATEWAY — element with value 502

    The enumeration element must have two methods:
        info() — method returning a two-element tuple containing the element
                 name and its value
        code_class() — method returning the name of the group in Russian
                       to which the element belongs

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the HTTPStatusCodes class, it can be arbitrary.
'''
from enum import Enum


class HTTPStatusCodes(Enum):
    """
    HTTP status codes enumeration.
    """
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self) -> tuple[str, int]:
        """
        Get name and value.

        Returns:
            tuple[str, int]: Name and status code.
        """
        return self.name, self.value

    def code_class(self) -> str:
        """
        Get group name.

        Returns:
            str: Group name (e.g., 'success').
        """
        groups = (
            'информация', 'успех',
            'перенаправление', 'ошибка клиента',
            'ошибка сервера'
        )
        return groups[(self.value // 100) - 1]

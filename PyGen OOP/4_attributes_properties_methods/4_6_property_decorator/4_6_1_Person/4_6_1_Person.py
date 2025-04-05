'''
TODO:
    You have access to the Person class, which describes a person.

    When instantiating the class, it takes two arguments in the following
    order:
        - name — the person's first name
        - surname — the person's last name

    An instance of the Person class has two attributes:
        - name — the person's first name
        - surname — the person's last name

    The Person class has one property:
        - fullname — a read-write property that returns the person's full name
                     as a string:
            <first name> <last name>

    Implement the fullname property of the Person class using the @property
    decorator.

NOTE:
    When a person's first and/or last name changes, their full name must also
    change.

    Similarly, when a person's full name changes, their first and last name
    must change.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.
'''


class Person:
    """
    A class representing a person with a first name and last name.

    Attributes:
        name (str): The person's first name.
        surname (str): The person's last name.

    Properties:
        fullname (str): A read-write property representing the full name as:
            '<first name> <last name>'.
    """

    def __init__(self, name: str, surname: str) -> None:
        """
        Initialize a Person instance with a first name and last name.

        Args:
            name (str): The person's first name.
            surname (str): The person's last name.
        """
        self.name: str = name
        self.surname: str = surname

    @property
    def fullname(self) -> str:
        """
        Get the person's full name.

        Returns:
            str: The full name as:
                '<first name> <last name>'.
        """
        return f"{self.name} {self.surname}"

    @fullname.setter
    def fullname(self, fullname: str) -> None:
        """
        Set the person's full name and update first name and last name.

        Args:
            fullname (str): The full name to set, expected as:
                '<first name> <last name>'.
        """
        self.name, self.surname = fullname.split()

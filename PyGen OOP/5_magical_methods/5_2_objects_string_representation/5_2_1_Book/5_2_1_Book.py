'''
TODO:
    It was required to implement a Book class that describes a book.

    When creating an instance, the class had to accept three arguments in
    the following order:
        - title — the title of the book
        - author — the author of the book
        - year — the year of the book's publication

    It was assumed that instances of the Book class would have the following
    formal string representation:
        Book('<book title>', '<book author>', <book publication year>)

    And the following informal string representation:
        <book title> (<book author>, <book publication year>)

    The programmer was in a hurry and solved the problem incorrectly.

    Correct the code below and implement the Book class correctly.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Book class,
    it can be arbitrary.
'''


class Book:
    """
    A class representing a book with title, author, and publication year.
    """

    def __init__(self, title: str, author: str, year: int) -> None:
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year of publication.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """
        Return an informal string representation of the book.

        Returns:
            str: The book in format '<title> (<author>, <year>)'.
        """
        return f"{self.title} ({self.author}, {self.year})"

    def __repr__(self) -> str:
        """
        Return a formal string representation of the book.

        Returns:
            str: The book in format "Book('<title>', '<author>', <year>)".
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

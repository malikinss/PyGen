'''
TODO:
    Implement the TitledText class, a subclass of str that describes text that
    has a title.

    When instantiating the class, it must accept two arguments in
    the following order:
        content — text
        text_title — text title

    The TitledText class must have one instance method:
        title() — a method that returns the text title

NOTE:
    The value of a TitledText class instance must be the text itself, not
    the text title or the text and title.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the TitledText
    class, it can be arbitrary.
'''
from typing import Any


class TitledText(str):
    """
    Class representing a string with an associated title.

    Inherits from str, with the string value being the content and a separate
    title attribute.
    """

    def __new__(cls, content: Any, text_title: Any) -> 'TitledText':
        """
        Create a new TitledText instance with the specified content and title.

        Args:
            content: The text content of the string.
            text_title: The title associated with the text.

        Returns:
            TitledText: A new instance with the content as its string value
                        and text_title as an attribute.
        """
        instance = super().__new__(cls, content)
        instance.text_title = text_title
        return instance

    def title(self) -> Any:
        """
        Return the title of the text.

        Returns:
            str: The title associated with the text.
        """
        return self.text_title

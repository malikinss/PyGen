'''
TODO:
    HTML is a markup language used to define the structure of web pages that
    users visit.

    HTML provides the means to create headings, paragraphs, links, quotes,
    and other elements.

    Each HTML element is marked with an opening and closing tag:
        <p>If a test isn't life-threatening, is it even science?</p>

    Tags are enclosed in angle brackets.

    They define where an element begins and ends.

    The only difference between an opening and closing tag is the slash that
    precedes the tag name.

    The opening and closing tags, as well as the content they contain,
    can be on the same line (example above) or on different lines.

    If the tags and content are on different lines, the opening tag is
    specified first, then the content is specified on the next line with
    an indent of two spaces, and then the closing tag is specified on the next
    line, which is located at the same indentation level as the opening tag:
        <p>
        Science does not answer the question Why?, it answers the question Why
        not?
        </p>

    Implement the HtmlTag class.

    When instantiated, the class must accept two arguments in the following
    order:
        tag — HTML tag
        inline — Boolean value, defaults to False

    An instance of the HtmlTag class must be a reentrant context manager that
    allows you to generate HTML code with correct indentation and tag nesting
    depth.

    The inline parameter must determine the position of the tags and their
    content.

    If it is True, the tags and content must be on the same line,
    if False — on different lines.

    The HtmlTag class must have one instance method:
        print() — a method that takes the tag content as an argument and
                  prints it within this tag

NOTE:
    Visual examples of using the HtmlTag class are demonstrated in the test
    data.

    Use two spaces as indents for each level.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    The HtmlTag class must satisfy the context manager protocol, that is,
    have __enter__() and __exit__() methods.

    The protocol implementation can be arbitrary.
'''
from typing import Optional, Type
from types import TracebackType


class HtmlTag:
    """
    A reentrant context manager for generating HTML with proper indentation
    and nesting.
    """

    level: int = -1  # Class-level nesting counter

    def __init__(self, tag: str, inline: bool = False) -> None:
        """
        Initialize with an HTML tag and inline formatting option.

        Args:
            tag: The HTML tag name (e.g., 'p', 'div').
            inline: Whether tags and content are on the same line.
                    Defaults to False.
        """
        self.tag: str = tag
        self.inline: bool = inline
        self._tag_indent: str = ''

    def __enter__(self) -> 'HtmlTag':
        """
        Enter the context manager, printing the opening tag with proper
        indentation.

        Returns:
            HtmlTag: The context manager instance for calling the print method.
        """
        HtmlTag.level += 1
        self._tag_indent = "  " * HtmlTag.level
        print(
            f"{self._tag_indent}<{self.tag}>",
            end='' if self.inline else '\n'
        )
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ) -> None:
        """
        Exit the context manager, printing the closing tag with proper
        indentation.

        Args:
            exc_type: Type of the exception, or None if no exception occurred.
            exc_value: The exception instance, or None.
            traceback: The traceback object, or None.
        """
        if self.inline:
            print(f"</{self.tag}>")
        else:
            print(f"{self._tag_indent}</{self.tag}>")
        HtmlTag.level -= 1

    def print(self, text: str) -> None:
        """
        Print the tag content with proper indentation.

        Args:
            text: The content to print within the tag.
        """
        if self.inline:
            print(text, end='')
        else:
            text_indent = self._tag_indent + '  '
            print(f"{text_indent}{text}")

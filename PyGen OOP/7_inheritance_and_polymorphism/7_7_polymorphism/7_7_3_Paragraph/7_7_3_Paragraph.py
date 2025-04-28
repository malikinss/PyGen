'''
TODO:
    A word is any sequence of one or more Latin letters.

    Implement the LeftParagraph class, which describes a paragraph aligned
    to the left.

    When creating an instance, the class must accept one argument:
        length — the length of the paragraph line

    The LeftParagraph class must have two instance methods:
        add() — a method that accepts a word or several words separated by
                a space as an argument and adds them to the current paragraph.
                If a word does not fit on the current line, it is carried over
                to the next line.
                The method must also automatically add one space after each
                added word (except the last one)
        end() — a method that prints the current paragraph aligned to the left.
                After calling the method, the current paragraph is considered
                empty, that is, the formation of a new one begins

    Also implement the RightParagraph class, which describes a paragraph
    aligned to the right.

    When creating an instance, the class must accept one argument:
        length — the length of the paragraph line

    The RightParagraph class must have two instance methods:
        add() — a method that accepts a word or several words separated by
                a space as an argument and adds them to the current paragraph.
                If a word does not fit on the current line, it is carried over
                to the next line.
                The method must also automatically add one space after each
                added word (except the last one)
        end() — a method that prints the current paragraph, right-aligned,
                taking into account the line length.
                After calling the method, the current paragraph is considered
                empty, that is, the formation of a new one begins

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented classes are used only with correct
    data.

    There are no restrictions regarding the implementation of classes,
    they can be arbitrary.
'''
from abc import ABC, abstractmethod


class Paragraph(ABC):
    """
    Abstract base for paragraph formatting.
    """

    def __init__(self, length: int) -> None:
        """
        Init with line length.

        Args:
            length: Line length.
        """
        self._len = length
        self._lines = [[]]

    def add(self, data: str) -> None:
        """
        Add words to paragraph.

        Args:
            data: Words separated by spaces.
        """
        for word in data.split():
            line = self._lines[-1]
            test = ' '.join(line + [word])
            if len(test) > self._len:
                self._lines.append([word])
            else:
                line.append(word)

    @abstractmethod
    def end(self) -> None:
        """
        Print and clear paragraph.
        """
        pass


class LeftParagraph(Paragraph):
    """
    Left-aligned paragraph.
    """

    def end(self) -> None:
        """
        Print left-aligned paragraph and clear.
        """
        for line in self._lines:
            if line:
                print(' '.join(line))
        self._lines = [[]]


class RightParagraph(Paragraph):
    """
    Right-aligned paragraph.
    """

    def end(self) -> None:
        """
        Print right-aligned paragraph and clear.
        """
        for line in self._lines:
            if line:
                print(' '.join(line).rjust(self._len))
        self._lines = [[]]

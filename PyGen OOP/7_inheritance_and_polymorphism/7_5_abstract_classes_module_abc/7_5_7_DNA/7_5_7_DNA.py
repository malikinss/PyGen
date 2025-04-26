'''
TODO:
    DNA consists of two chains oriented with their nitrogenous bases facing
    each other.

    There are four types of nitrogenous bases in DNA:
        adenine (A), guanine (G), thymine (T), and cytosine (C).

    The nitrogenous bases of one chain are linked to the nitrogenous bases of
    the other chain by hydrogen bonds according to the principle of
    complementarity:
        adenine (A) is linked only to thymine (T),
        guanine (G) is linked only to cytosine (C).

    Implement a DNA class that describes a double-stranded DNA helix.

    When creating an instance, the class must accept one argument:
        chain — the first DNA chain, which is a string of the characters:
                    A, G, T, and C (nitrogenous bases)

    An instance of the DNA class must have the following informal string
    representation:
        <nitrogenous bases of the first DNA chain>

    When passing an instance of the DNA class to the len() function,
    the number of nitrogenous bases in one of its chains must be returned.

    When passing an instance of the class to the reversed() function,
    an iterator must be returned whose elements are the elements of the passed
    instance of the DNA class, arranged in reverse order.

    In addition, an instance of the DNA class must be an iterable object,
    that is, it must allow its elements to be iterated over, for example,
    using a for loop.

    Also, an instance of the DNA class must allow the values of its elements
    to be obtained using indices, both positive and negative.

    In the case of the reversed() function, iteration, and index access,
    the elements of a DNA instance must be represented as tuples of
    two elements, the first of which is the base of the first DNA strand at
    the specified index, and the second is the nitrogenous base of the second
    DNA strand at the specified index.

    The nitrogenous base of the second DNA strand can be obtained using
    the principle of complementarity.

    In addition, a DNA instance must support the membership operation using
    the in operator.

    In this case, it must check whether the nitrogenous base is in the first
    DNA strand.

    DNA instances must support comparison operations with each other using
    the == and != operators.

    Two DNAs are considered equal if their first strands match.

    Finally, DNA instances must support addition with each other using
    the + operator, which results in a new DNA instance whose first strand is
    the concatenation of the first strands of the original DNA instances.

NOTE:
    Before making a decision, think about which abstract class from
    the collections.abc module would be convenient as a parent.

    If the object with which the comparison or addition operation is performed
    is invalid, the method implementing this operation must return
    the NotImplemented constant.

    There are no restrictions regarding the implementation of the DNA class,
    it can be arbitrary.
'''
from collections.abc import Sequence, Iterator
from typing import Any, Union


class DNA(Sequence):
    """Class representing a double-stranded DNA helix.

    Stores the first strand and provides access to complementary pairs.
    """

    _PAIRS = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    def __init__(self, chain: str) -> None:
        """
        Initialize DNA with the first strand.

        Args:
            chain: String of nitrogenous bases (A, G, T, C).
        """
        self._first = chain

    def __str__(self) -> str:
        """
        Return the first DNA strand.

        Returns:
            str: First strand as a string.
        """
        return self._first

    def __len__(self) -> int:
        """
        Return the number of bases in one strand.

        Returns:
            int: Length of the strand.
        """
        return len(self._first)

    def __getitem__(
        self, key: Union[int, slice]
    ) -> Union[tuple[str, str], Sequence[tuple[str, str]]]:
        """
        Access base pair(s) by index or slice.

        Args:
            key: Index or slice for accessing bases.

        Returns:
            tuple[str, str] | Sequence[tuple[str, str]]:
             Base pair or sequence of pairs.
        """
        base = self._first[key]
        if isinstance(key, slice):
            return [(b, self._PAIRS[b]) for b in base]
        return (base, self._PAIRS[base])

    def __iter__(self) -> Iterator[tuple[str, str]]:
        """
        Iterate over base pairs.

        Returns:
            Iterator[tuple[str, str]]: Iterator of (first, second) base pairs.
        """
        return ((base, self._PAIRS[base]) for base in self._first)

    def __reversed__(self) -> Iterator[tuple[str, str]]:
        """
        Iterate over base pairs in reverse order.

        Returns:
            Iterator[tuple[str, str]]: Reverse iterator of base pairs.
        """
        return (
            (base, self._PAIRS[base])
            for base in reversed(self._first)
        )

    def __contains__(self, value: Any) -> bool:
        """
        Check if a base is in the first strand.

        Args:
            value: Base to check.

        Returns:
            bool: True if base is in the first strand.
        """
        return value in self._first

    def __eq__(self, other: Any) -> bool:
        """
        Check if two DNAs have identical first strands.

        Args:
            other: Object to compare.

        Returns:
            bool: True if first strands match, NotImplemented otherwise.
        """
        if not isinstance(other, DNA):
            return NotImplemented
        return self._first == other._first

    def __add__(self, other: Any) -> 'DNA':
        """
        Concatenate two DNAs by their first strands.

        Args:
            other: DNA to concatenate.

        Returns:
            DNA: New DNA with concatenated first strands, or NotImplemented.
        """
        if not isinstance(other, DNA):
            return NotImplemented
        return DNA(self._first + other._first)

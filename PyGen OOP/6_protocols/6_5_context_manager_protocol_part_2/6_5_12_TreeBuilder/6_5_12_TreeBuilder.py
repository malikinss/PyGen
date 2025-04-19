'''
TODO:
    Implement the TreeBuilder class.

    The class must not take any arguments when instantiated.

    A TreeBuilder instance must be a reentrant context manager that allows you
    to build a tree data structure (tree) step by step.

    The TreeBuilder class must have two instance methods:
        - add() — a method that takes an arbitrary object (leaf) as
                  an argument and adds it to the current tree node
        - structure() — a method that returns the tree structure as nested
                        lists

    Adding nodes to a tree must be done using the with operator.

    A node is considered current within its with block.

    If no leaves have been added to a node, then this node must not appear in
    the tree structure returned by the structure() method.

NOTE:
    The tree structure can be arbitrary, that is, a node can contain another
    node, which in turn can contain another, and so on.

    It is guaranteed that the tree structure is not displayed inside with
    blocks, that is, the tree structure is displayed only after it has been
    built.

    Illustrative examples of using the TreeBuilder class are demonstrated in
    the test data.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    The TreeBuilder class must satisfy the context manager protocol, that is,
    have the __enter__() and __exit__() methods.

    The protocol implementation can be arbitrary.
'''
from typing import Any, Optional, Type
from types import TracebackType


class TreeBuilder:
    """
    A reentrant context manager for building a tree structure as nested lists.
    """

    def __init__(self) -> None:
        """
        Initialize an empty tree structure.
        """
        self._tree: list[list[Any]] = [[]]

    def __enter__(self) -> 'TreeBuilder':
        """
        Enter the context manager, creating a new tree node.

        Returns:
            TreeBuilder: The instance for adding leaves or nested nodes.
        """
        self._tree.append([])
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ) -> None:
        """
        Exit the context manager, adding the current node to its parent if
        non-empty.

        Args:
            exc_type: Type of the exception, or None if no exception occurred.
            exc_value: The exception instance, or None.
            traceback: The traceback object, or None.
        """
        current_node = self._tree.pop()
        if current_node:
            self._tree[-1].append(current_node)

    def add(self, obj: Any) -> None:
        """
        Add a leaf to the current tree node.

        Args:
            obj: The object to add as a leaf.
        """
        self._tree[-1].append(obj)

    def structure(self) -> list[Any]:
        """
        Return the tree structure as nested lists.

        Returns:
            list[Any]: The root node of the tree as a list of leaves and
                       nested nodes.
        """
        return self._tree[0]

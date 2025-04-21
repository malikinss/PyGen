'''
TODO:
    Implement a FieldTracker class that allows children to track the state of
    certain attributes of their class instances.

    Children must inherit four instance methods:
        base() — a method that takes an attribute name as an argument and
                 returns either the current value of the attribute or
                 the original (specified when defining) value of the attribute
                 if it has changed
        has_changed() — a method that takes an attribute name as an argument
                        and returns True if the value of the attribute has
                        changed at least once, or False otherwise
        changed() — a method that returns a dictionary whose keys are
                    the names of the attributes that have changed their values,
                    and whose values are their original values
        save() — a method that resets tracking. After calling the method,
                 it is assumed that all attributes have not changed their
                 values before, and their current values are considered initial

    It is guaranteed that the heirs of the FieldTracker class:
        - always have a fields class attribute containing a tuple with
          the attributes that need to be tracked
        - always call the FieldTracker class initializer in their initializer
          after setting the primary values of the tracked attributes

NOTE:
    We will assume that the attribute changes its value only if the value
    being set differs from the current one.

    The implementation of the FieldTracker class can be arbitrary, that is,
    there are no requirements for the presence of certain attributes.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from typing import Any, Dict


class FieldTracker:
    """
    Class providing attribute state tracking for subclasses.

    Subclasses must define a `fields` tuple with attribute names to track and
    call this class's `__init__` after setting initial attribute values.
    """

    def __init__(self) -> None:
        """
        Initialize a FieldTracker instance.

        Creates a history dictionary to store initial values of tracked
        attributes.
        """
        self._history = {
            attr: getattr(self, attr)
            for attr in self.fields
        }

    def base(self, attr: str) -> Any:
        """
        Return the initial value of the specified attribute.

        Args:
            attr: The name of the attribute to check.

        Returns:
            Any: The initial value of the attribute.
        """
        return self._history[attr]

    def has_changed(self, attr: str) -> bool:
        """
        Check if the specified attribute has changed.

        Args:
            attr: The name of the attribute to check.

        Returns:
            bool: True if the attribute's value has changed, False otherwise.
        """
        return self.base(attr) != getattr(self, attr)

    def changed(self) -> Dict[str, Any]:
        """
        Return a dictionary of changed attributes and their initial values.

        Returns:
            Dict[str, Any]: A dictionary with names of changed attributes as
                            keys and their initial values as values.
        """
        return {
            attr: self.base(attr)
            for attr in self.fields
            if self.has_changed(attr)
        }

    def save(self) -> None:
        """
        Reset tracking by updating initial values to current values.
        """
        for attr in self.fields:
            self._history[attr] = getattr(self, attr)

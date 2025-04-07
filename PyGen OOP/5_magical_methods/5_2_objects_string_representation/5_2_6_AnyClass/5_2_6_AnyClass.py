'''
TODO:
    Implement the AnyClass class.

    When creating an instance, the class must accept an arbitrary number of
    named arguments and set them as attributes of the created instance.

    An instance of the AnyClass class must have the following formal string
    representation:
        AnyClass(
            <name of the 1st attribute>=<value of the 1st attribute>,
            <name of the 2nd attribute>=<value of the 2nd attribute>,
            ...
        )

    And the following informal string representation:
        AnyClass: <name of the 1st attribute>=<value of the 1st attribute>,
                  <name of the 2nd attribute>=<value of the 2nd attribute>,
                  ...

NOTE:
    Note that attribute values that belong to the str type must be enclosed in
    single quotation marks.

    There are no restrictions on the implementation of the AnyClass class,
    it can be arbitrary.
'''


class AnyClass:
    """
    A class that accepts arbitrary named arguments and sets them as attributes.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initialize an AnyClass instance with named arguments.

        Args:
            **kwargs: Arbitrary named arguments to set as attributes.
        """
        self.__dict__.update(kwargs)

    def _format_attrs(self) -> str:
        """
        Format attributes as a comma-separated string with strings in quotes.

        Returns:
            str: Formatted attributes, e.g., "a='foo', b=42".
        """
        attrs = []
        for key, value in self.__dict__.items():
            if isinstance(value, str):
                value = f"'{value}'"
            attrs.append(f"{key}={value}")
        return ", ".join(attrs)

    def __repr__(self) -> str:
        """
        Return a formal string representation of the instance.

        Returns:
            str: The instance in format:
                    'AnyClass(<key1>=<value1>, <key2>=<value2>, ...)'.
        """
        return f"AnyClass({self._format_attrs()})"

    def __str__(self) -> str:
        """
        Return an informal string representation of the instance.

        Returns:
            str: The instance in format:
                'AnyClass: <key1>=<value1>, <key2>=<value2>, ...'.
        """
        return f"AnyClass: {self._format_attrs()}"

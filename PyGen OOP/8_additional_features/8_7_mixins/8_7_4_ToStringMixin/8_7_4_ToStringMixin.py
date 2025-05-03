'''
TODO:
    Implement a ToStringMixin class that adds the following formal and
    informal string representation to class instances:
        <class name>(<class instance attribute dictionary>)

    If a class instance has more than 6 attributes, the dictionary of
    attributes in formal and informal string representation must have
    the following format:
        {
            <attribute 1>: <value 1>,
            <attribute 2>: <value 2>,
            <attribute 3>: <value 3>,
            <attribute 4>: <value 4>,
            <attribute 5>: <value 5>,
            <attribute 6>: <value 6>,
            ...
        }

NOTE:
    Attributes in formal and informal string representation must be specified
    in the same order in which they were added to the instance.

    No additional data validation is required.

    The implemented class is guaranteed to be used only with valid data.

    There are no restrictions regarding the implementation of
    the ToStringMixin class, it can be arbitrary.
'''
from typing import List, Tuple, Any, Iterator


class ToStringMixin:
    """
    A mixin class for custom string representation of instance attributes.
    """
    def __repr__(self) -> str:
        """
        Return formal string representation: <class>({'attr': value, ...}).
        """
        cls_name = self.__class__.__name__
        attrs = self.__dict__
        attr_items = list(attrs.items())

        if len(attrs) > 6:
            # Limit to first 6 attributes, add '...'
            attr_str = ', '.join(
                self._format_attrs(attr_items[:6])
            )
            return f"{cls_name}({{{attr_str}, ...}})"

        attr_str = ', '.join(self._format_attrs(attr_items))
        return f"{cls_name}({{{attr_str}}})"

    def _format_attrs(
        self, attrs: List[Tuple[str, Any]]
    ) -> Iterator[str]:
        """
        Format attribute key-value pairs for string representation.

        Args:
            attrs: List of (key, value) tuples for attributes.

        Returns:
            Iterator of formatted strings for each attribute.
        """
        return (f"{k!r}: {v!r}" for k, v in attrs)

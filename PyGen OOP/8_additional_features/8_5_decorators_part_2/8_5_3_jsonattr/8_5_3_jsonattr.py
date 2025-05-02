'''
TODO:
    Implement the @jsonattr decorator to decorate the class.

    The decorator must accept one argument:
        filename — the name of the json file whose contents are a JSON object

    The decorator must open the file filename and add each key-value pair of
    the JSON object contained in that file as an attribute to the decorated
    class.
'''
import json
from typing import Type, TypeVar

T = TypeVar("T")


class jsonattr:
    """
    Decorator to add JSON attributes to a class.
    """
    def __init__(self, filename: str) -> None:
        """
        Init decorator.

        Args:
            filename: JSON file with object to load.
        """
        with open(filename, 'r') as file:
            self.attrs = json.load(file)

    def __call__(self, cls: Type[T]) -> Type[T]:
        """
        Add JSON attributes to the class.

        Args:
            cls: Class to decorate.

        Returns:
            Type[T]: Decorated class.
        """
        for attr, value in self.attrs.items():
            setattr(cls, attr, value)
        return cls

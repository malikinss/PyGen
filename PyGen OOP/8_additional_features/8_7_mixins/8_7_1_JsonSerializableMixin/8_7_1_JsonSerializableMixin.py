'''
TODO:
    Implement the JsonSerializableMixin class, which adds the functionality of
    serializing class instances to JSON format to classes.

    The JsonSerializableMixin class must have one instance method:
        to_json() — a method that returns a JSON representation of the class
                    instance

    The JSON representation of the class instance must be a json-format string
    obtained by serializing the dictionary of attributes of the class instance.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the JsonSerializableMixin class, it can be arbitrary.
'''
import json


class JsonSerializableMixin:
    """
    A mixin class for JSON serialization of instance attributes.
    """
    def to_json(self) -> str:
        """
        Return a JSON string of the instance's attributes.
        """
        return json.dumps(self.__dict__)

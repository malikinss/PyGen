'''
TODO:
    Implement a MultiKeyDict class that is almost identical to the dict class.

    Creating an instance of the MultiKeyDict class should be similar
    to creating an instance of the dict class:
        multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
        multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])
        print(multikeydict1['x']) # 1
        print(multikeydict2['z']) # 3

    A special feature of the MultiKeyDict class should be the alias() method,
    which should allow you to give aliases to existing keys.

    Access by the created alias should not differ in any way from access by
    the original key, i.e. from the moment the alias is created the value has
    two keys (or more, if there are several aliases):
        multikeydict = MultiKeyDict(x=100, y=[10, 20])
        multikeydict.alias('x', 'z') # adding alias 'z' to key 'x'
        multikeydict.alias('x', 't') # adding alias 't' to key 'x'
        print(multikeydict['z']) # 100
        multikeydict['t'] += 1
        print(multikeydict['x']) # 101
        multikeydict.alias('y', 'z') # now 'z' becomes an alias of key 'y'
        multikeydict['z'] += [30]
        print(multikeydict['y']) # [10, 20, 30]

    The value must remain accessible via the alias even if the original key
    has been deleted:
        multikeydict = MultiKeyDict(x=100)
        multikeydict.alias('x', 'z')
        del multikeydict['x']
        print(multikeydict['z']) # 100

    Keys must take precedence over aliases.

    If some key and alias are the same, then all operations on them must be
    performed with the key:
        multikeydict = MultiKeyDict(x=100, y=[10, 20])
        multikeydict.alias('x', 'y')
        print(multikeydict['y']) # [10, 20]
'''
from collections import UserDict
from typing import Hashable, Any


class MultiKeyDict(UserDict):
    """
    Dictionary with support for key aliases.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize with empty aliases.
        """
        self.aliases: dict[Hashable, Hashable] = {}
        super().__init__(*args, **kwargs)

    def __getitem__(self, key: Hashable) -> Any:
        """
        Get value by key or alias.

        Args:
            key: Key or alias to access value.

        Returns:
            Value associated with key or alias.

        Raises:
            KeyError: If key or alias does not exist.
        """
        if key in self.data:
            return self.data[key]
        if key in self.aliases:
            return self.data[self.aliases[key]]
        raise KeyError(key)

    def __setitem__(
        self, key: Hashable, value: Any
    ) -> None:
        """
        Set value for key or alias.

        Args:
            key: Key or alias to set value.
            value: Value to set.
        """
        if key in self.data:
            self.data[key] = value
        elif key in self.aliases:
            self.data[self.aliases[key]] = value
        else:
            self.data[key] = value

    def __delitem__(self, key: Hashable) -> None:
        """
        Delete key, preserving value via alias if exists.

        Args:
            key: Key to delete.

        Raises:
            KeyError: If key does not exist.
        """
        if key not in self.data:
            raise KeyError(key)
        # Find an alias for the key, if any
        new_key = next(
            (
                k
                for k, v in self.aliases.items()
                if v == key
            ),
            None
        )
        if new_key is not None:
            # Move value to alias and update aliases
            self.data[new_key] = self.data[key]
            del self.data[key]
            for k in list(self.aliases):
                if self.aliases[k] == key:
                    self.aliases[k] = new_key
        else:
            del self.data[key]

    def alias(
        self, key: Hashable, new_name: Hashable
    ) -> None:
        """
        Add alias to existing key.

        Args:
            key: Existing key to alias.
            new_name: New alias for the key.

        Raises:
            KeyError: If key does not exist.
        """
        if key not in self.data:
            raise KeyError(key)
        # Remove new_name if it’s an alias for another key
        if new_name in self.aliases:
            del self.aliases[new_name]
        self.aliases[new_name] = key

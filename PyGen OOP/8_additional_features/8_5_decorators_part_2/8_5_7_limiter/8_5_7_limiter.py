'''
TODO:
    By default, any user-defined class can create an infinite number of its
    own instances.

    The singleton design pattern, on the other hand, ensures that a class
    has only one instance of itself, and that any attempt to create a new
    instance returns the existing one.

    Implement the @limiter decorator to decorate a class that limits
    the number of instances created by the decorated class to a certain number.

    The decorator must take three arguments in the following order:
        limit — the number of instances that the decorated class can create
        unique — the name of an instance attribute of the decorated class
                 whose value is its identifier.
                 Two instances with the same identifier cannot exist.
                 If an attempt is made to create an instance whose identifier
                 matches the identifier of a previously created instance,
                 that previously created instance must be returned
        lookup — determines which object should be returned if the limit is
                 exceeded and the unique attribute value has not been used
                 before.
                 If FIRST is returned, the very first instance created is
                 returned; if LAST is returned, the very last instance created
                 is returned

NOTE:
    Instances of the decorated class are guaranteed to always have
    an attribute that contains their identifier.
'''


from typing import Any, Callable, Dict, Type, TypeVar

T = TypeVar("T")


class limiter:
    """
    Decorator to limit the number of class instances.
    """
    def __init__(self, limit: int, unique: str, lookup: str) -> None:
        """
        Initialize the limiter decorator.

        Args:
            limit: Maximum number of instances allowed.
            unique: Name of the instance attribute used as identifier.
            lookup: Return mode ('FIRST' or 'LAST') when limit is exceeded.
        """
        self.limit: int = limit
        self.unique: str = unique
        self.lookup: str = lookup
        self.instances: Dict[str, T] = {}
        self.lookups: Dict[str, T] = {}
        self.cls: Type[T] | None = None

    def __call__(
        self, cls: Type[T]
    ) -> Callable[..., T]:
        """
        Decorate the class to limit instance creation.

        Args:
            cls: Class to decorate.

        Returns:
            Callable[..., T]: Function to create or return instances.
        """
        self.cls = cls
        return self.get_instance

    def get_instance(self, *args: Any, **kwargs: Any) -> T:
        """
        Create or return an instance based on limit and identifier.

        Args:
            *args: Positional arguments for class initialization.
            **kwargs: Keyword arguments for class initialization.

        Returns:
            T: New or existing instance.
        """
        instance = self.cls(*args, **kwargs)

        # Set the first instance if not already set
        self.lookups.setdefault('FIRST', instance)

        # Get the unique identifier from the instance
        identifier = getattr(instance, self.unique)

        if len(self.instances) < self.limit:
            # Add new instance if identifier is unique
            if identifier not in self.instances:
                # Store instance in instances and update last lookup
                self.instances[identifier] = instance
                self.lookups['LAST'] = instance
            return self.instances[identifier]

        # Return existing instance or fallback based on lookup mode
        existing_instance = self.instances.get(identifier)
        return existing_instance or self.lookups.get(self.lookup)

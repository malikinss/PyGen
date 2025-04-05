'''
TODO:
    Implement a Config class that follows the singleton pattern and describes
    a configuration object with fixed parameters.

    The class must not take any arguments when instantiated.

    The first call to the Config class must create and return an instance of
    this class, and subsequent calls must return the instance created during
    the first call.

    An instance of the Config class must have four attributes:
        - program_name — an attribute with the string value GenerationPy
        - environment — an attribute with the string value release
        - loglevel — an attribute with the string value verbose
        - version — an attribute with the string value 1.0.0

NOTE:
    There are no restrictions regarding the implementation of the Config class,
    it can be arbitrary.
'''


class Config:
    """
    A singleton class representing a fixed configuration.
    """
    _instance = None
    _initialized = False

    def __new__(cls) -> 'Config':
        """
        Create or return the singleton instance of Config.

        Returns:
            Config: The singleton instance of the Config class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """
        Initialize the Config instance only once.

        Sets:
            program_name (str): Set to 'GenerationPy'.
            environment (str): Set to 'release'.
            loglevel (str): Set to 'verbose'.
            version (str): Set to '1.0.0'.
        """
        if not Config._initialized:
            self.program_name = "GenerationPy"
            self.environment = "release"
            self.loglevel = "verbose"
            self.version = "1.0.0"
            Config._initialized = True

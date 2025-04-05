# Config Class Singleton Settings

## Description 📝

The `Config` class implements the singleton pattern to provide a single, shared configuration object with fixed parameters.
It requires no instantiation arguments and ensures only one instance exists, initialized with predefined attributes on the first creation.

## Purpose 🎯

This class is designed for managing global configuration settings, suitable for applications needing consistent configuration access, educational examples of the singleton pattern, or systems requiring immutable settings.

## How It Works 🔍

-   ****new**() Method**: Overrides object creation to return the existing `_instance` if it exists, or creates a new one if `_instance` is `None`.
-   ****init**() Method**: Initializes attributes only on the first call, using a `_initialized` flag to prevent reinitialization:
    -   `program_name`: Set to `"GenerationPy"`.
    -   `environment`: Set to `"release"`.
    -   `loglevel`: Set to `"verbose"`.
    -   `version`: Set to `"1.0.0"`.
-   **Class Attributes**: `_instance` stores the singleton object; `_initialized` tracks initialization state.

## Usage 📦

1. Save the class in a Python file, e.g., `config.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from config import Config
config1 = Config()
config2 = Config()
print(f"Program Name: {config1.program_name}")
print(f"Version: {config2.version}")
print(f"Same instance: {config1 is config2}")
```

## Conclusion 🚀

The `Config` class ensures a single, consistent configuration instance in Python using the singleton pattern, providing easy access to fixed settings.
Its design is straightforward and can be extended with additional attributes or methods for more complex configuration management.

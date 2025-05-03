# snake_case Decorator Class Implementation

## Description 📝

The provided code implements the `snake_case` decorator as a class that renames non-magic methods (and optionally attributes) of a decorated class from Camel Case or lower Camel Case to Snake Case.
The decorator takes a boolean argument `attrs` to determine whether class attributes should also be renamed.
It uses regular expressions in a helper class `CaseHelper` to identify and convert names, ensuring only valid Camel Case names are renamed while preserving leading underscores and skipping magic methods (dunder methods).

## Purpose 🎯

Intended for scenarios requiring consistent naming conventions, such as code standardization, API design, or educational examples of Python class decorators, regular expressions, and dynamic attribute manipulation.

## How It Works 🔍

-   **CaseHelper Class**:
    -   A utility class with static methods for string case detection and conversion:
        -   `is_snake(string)`: Checks if a string is in Snake Case (e.g., `bee_geek`) using regex `^[a-z]+(_[a-z]+)*$`.
        -   `is_camel(string)`: Checks if a string is in Camel Case or lower Camel Case (e.g., `BeeGeek`, `beeGeek`) using regex `^[a-z]+([A-Z][a-z0-9]*)*$|^([A-Z][a-z0-9]+)+$`, ignoring leading underscores.
        -   `is_dunder(string)`: Checks if a string is a magic method (e.g., `__init__`) using regex `^__\w+__$`.
        -   `_extract_leading_underscores(string)`: Extracts leading underscores (e.g., `_FirstMethod` → `_`).
        -   `to_snake(string)`: Converts Camel Case to Snake Case (e.g., `BeeGeek` → `bee_geek`), preserving leading underscores by inserting underscores before capital letters and converting to lowercase.
-   **snake_case Class**:
    -   **Initialization (`__init__`)**:
        -   Takes `attrs` (boolean, default `False`) to determine if attributes should be renamed.
        -   Stores `attrs` as `self.attrs`.
    -   **Call Method (`__call__`)**:
        -   Takes `cls` (the class to decorate).
        -   Iterates over `cls.__dict__` to inspect class attributes and methods.
        -   For each name-value pair:
            -   Checks if the name is Camel Case (`CaseHelper.is_camel`) and not a dunder method (`CaseHelper.is_dunder`).
            -   Identifies methods (callable or `classmethod`/`staticmethod`) and attributes (if `self.attrs` is `True`).
            -   Collects names to rename in `to_rename` with their values and new Snake Case names (`CaseHelper.to_snake`).
        -   Performs renaming by:
            -   Setting new attributes with `setattr(cls, new_name, value)`.
            -   Deleting old attributes with `delattr(cls, old_name)` if the name changed, handling potential `AttributeError`.
        -   Returns the modified `cls`.
-   **Behavior**:
    -   Renames non-magic methods from Camel Case/lower Camel Case to Snake Case.
    -   Optionally renames attributes if `attrs=True`.
    -   Preserves leading underscores and skips Snake Case or dunder names.
    -   Supports arbitrary class structures (methods, classmethods, staticmethods, attributes).
    -   No validation is performed, as inputs are guaranteed to be valid Camel Case, lower Camel Case, or Snake Case names.

## Verification ✅

Implementation satisfies requirements:

-   **Decorator Class**:
    -   `snake_case` is a class that takes a boolean `attrs` argument (default `False`) and decorates a class.
-   **Method Renaming**:
    -   Renames non-magic methods from Camel Case (`BeeGeek`) or lower Camel Case (`beeGeek`) to Snake Case (`bee_geek`).
    -   Example: `GetData` → `get_data`, `getData` → `get_data`.
    -   Skips dunder methods (e.g., `__init__`) and Snake Case methods (e.g., `already_snake`).
-   **Attribute Renaming**:
    -   If `attrs=True`, renames attributes from Camel Case/lower Camel Case to Snake Case.
    -   If `attrs=False`, leaves attributes unchanged.
    -   Example: `VersionNumber` → `version_number` (if `attrs=True`).
-   **Correctness**:
    -   Uses `CaseHelper.is_camel` to identify Camel Case/lower Camel Case names.
    -   Uses `CaseHelper.to_snake` to convert names, preserving leading underscores.
    -   Handles `classmethod` and `staticmethod` correctly.
    -   Deletes old names to avoid duplication.
    -   No validation needed per requirements.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `CaseHelper.is_camel` accurately identifies Camel Case and lower Camel Case, ignoring leading underscores.
    -   `CaseHelper.to_snake` correctly converts names by inserting underscores before capitals and lowercasing.
    -   `is_dunder` ensures magic methods are skipped.
    -   `setattr` and `delattr` handle attribute renaming robustly, bypassing `mappingproxy` restrictions.
    -   Checking `callable` or `classmethod`/`staticmethod` ensures only methods and specified attributes are renamed.
-   **Performance**:
    -   Initialization: O(1) for storing `attrs`.
    -   `__call__`: O(n) for iterating `cls.__dict__` (n is number of attributes/methods), O(m) for renaming (m is number of renamed items), plus regex operations.
    -   Regex operations (`is_camel`, `to_snake`) are efficient for typical method/attribute names.
    -   Suitable for most class sizes.
-   **Design**:
    -   Class-based decorator is explicit and aligns with requirements.
    -   `CaseHelper` encapsulates regex logic for clarity and reusability.
    -   Type hints (`Type[T]`, `TypeVar`, `str`, `bool`) clarify inputs and outputs.
    -   Two-pass approach (collect then rename) avoids modifying `__dict__` during iteration.
-   **Alternatives**:
    -   Function-based decorator: Possible but less aligned with class-based requirement.
    -   Manual string parsing without regex: Error-prone and less robust.
    -   Modifying `__dict__` directly: Not possible due to `mappingproxy`.
    -   Renaming during iteration: Risky due to dictionary modification.
-   **Extensibility**:
    -   Easily extended to support other naming conventions (e.g., kebab-case).
    -   Could add validation for name formats or log renaming actions.
-   **Edge Cases**:
    -   Empty `__dict__`: No renaming occurs, class returned unchanged.
    -   Snake Case names: Skipped, as they don’t need conversion.
    -   Dunder methods: Explicitly excluded to preserve special behavior.
    -   Leading underscores: Preserved in converted names (e.g., `_GetData` → `_get_data`).
    -   Classmethods/staticmethods: Handled correctly by checking type.
    -   Attribute conflicts: `setattr` overwrites, `delattr` removes old names.

## Usage Example (For Clarity, Not Submission) 📦

```python
@snake_case()
class MyClass:
    def GetData(self):
        return "data"

    def processData(self):
        return "processed"

    def already_snake(self):
        return "snake"

    VersionNumber = 1

# Test method renaming
print(hasattr(MyClass, "get_data"))  # True
print(hasattr(MyClass, "process_data"))  # True
print(hasattr(MyClass, "already_snake"))  # True
print(hasattr(MyClass, "GetData"))  # False
print(MyClass().get_data())  # data

# Test attribute preservation
print(MyClass.VersionNumber)  # 1 (unchanged, attrs=False)

# Test with attrs=True
@snake_case(attrs=True)
class AnotherClass:
    def HelloWorld(self):
        return "hello"

    AppVersion = "1.0"
    UserCount = 100

print(hasattr(AnotherClass, "hello_world"))  # True
print(hasattr(AnotherClass, "app_version"))  # True
print(hasattr(AnotherClass, "user_count"))  # True
print(AnotherClass.app_version)  # 1.0
print(AnotherClass.user_count)  # 100

# Test classmethod and leading underscores
@snake_case(attrs=True)
class SpecialClass:
    @classmethod
    def _GetInfo(cls):
        return "info"

    _MaxSize = 42

print(hasattr(SpecialClass, "_get_info"))  # True
print(hasattr(SpecialClass, "_max_size"))  # True
print(SpecialClass._get_info())  # info
```

## Conclusion 🚀

The `snake_case` decorator class implementation is precise, correctly renaming non-magic methods (and optionally attributes) from Camel Case/lower Camel Case to Snake Case.
It uses robust regex-based detection and conversion via `CaseHelper`, preserves leading underscores, skips dunder methods, and handles classmethods/staticmethods.
The design is efficient, extensible, and ideal for enforcing naming conventions or teaching decorator concepts, fully compliant with the task’s requirements.

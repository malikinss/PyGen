# NonKeyword Class Keyword-Restricting Descriptor

## Description 📝

The `NonKeyword` class is a descriptor that manages an attribute, ensuring its value is not a Python keyword string.
It accepts a `name` argument during instantiation, representing the attribute name.
When accessing the attribute, it returns the stored value or raises `AttributeError` with "Attribute not found" if unset.
When setting the attribute, it checks if the value is a Python keyword string, raising `ValueError` with "Invalid value" if it is, otherwise storing the value.

## Purpose 🎯

Designed for scenarios requiring restricted attribute values, such as configuration objects, domain-specific models, or validation in frameworks, where Python keywords must be avoided to prevent naming conflicts or semantic issues.
It’s also suitable for educational examples demonstrating Python’s descriptor protocol and keyword validation.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts `name` (string) and stores it as `self._attr`.
-   **Set Name Method (`__set_name__`)**:
    -   Automatically called when the descriptor is assigned in a class.
    -   Updates `self._attr` with the attribute name, ensuring consistency.
-   **Get Method (`__get__`)**:
    -   If `obj` is `None` (class access), returns the descriptor instance.
    -   If the attribute exists in `obj.__dict__`, returns its value.
    -   Otherwise, raises `AttributeError` with "Attribute not found".
-   **Set Method (`__set__`)**:
    -   Checks if `value` is a Python keyword string using `__is_string_keyword`.
    -   If it is, raises `ValueError` with "Invalid value".
    -   Otherwise, stores `value` in `obj.__dict__[self._attr]`.
-   **Helper Method (`__is_string_keyword`)**:
    -   Returns `True` if `value` is a string and a Python keyword (via `keyword.iskeyword`), `False` otherwise.
-   **Behavior**:
    -   Enforces non-keyword values for the attribute.
    -   Provides standard descriptor access and mutation with appropriate errors.

## Verification ✅

Implementation satisfies requirements:

-   **Attribute Access**:
    -   `obj.x` returns the value if set, else raises `AttributeError: Attribute not found`.
    -   E.g., `obj.x = "valid"; print(obj.x)` yields `"valid"`.
-   **Attribute Setting**:
    -   `obj.x = "if"` raises `ValueError: Invalid value`.
    -   `obj.x = "hello"` sets the value successfully.
    -   Non-string values (e.g., `42`, `None`) are allowed, as they aren’t keywords.
-   **Keyword Check**:
    -   Correctly identifies Python keywords (e.g., `"if"`, `"for"`) using `keyword.iskeyword`.
    -   Non-keyword strings (e.g., `"data"`) are permitted.
-   **Descriptor Protocol**: `__get__` and `__set__` (with `__set_name__`) ensure proper attribute management.

## Potential Considerations 🛠️

-   **Correctness**: `keyword.iskeyword` is the standard way to check Python keywords; `isinstance(value, str)` ensures only string keywords are blocked.
-   **Performance**: Keyword lookup and dictionary access are O(1), making operations efficient.
-   **Design**: Storing values in `obj.__dict__` is standard for non-data descriptors; `__set_name__` enhances compatibility with modern Python.

## Usage Example (For Clarity, Not Submission) 📦

```python
class Test:
    x = NonKeyword("x")

obj = Test()
obj.x = "hello"  # Sets successfully
print(obj.x)  # hello
obj.x = "if"  # Raises ValueError: Invalid value
print(obj.x)  # hello
obj.x = 42  # Sets successfully
print(obj.x)  # 42
del obj.x
print(obj.x)  # Raises AttributeError: Attribute not found
```

## Conclusion 🚀

The `NonKeyword` implementation is precise, enforcing non-keyword attribute values with clear error handling.
It’s ideal for controlled attribute management or descriptor education, fully compliant with the task’s requirements.

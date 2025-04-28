# get_method_owner Function Implementation

## Description 📝

The provided code implements the `get_method_owner` function, which takes a class (`cls`) and a method name (`method`) as arguments. It returns the class in the inheritance hierarchy of `cls` that defines the specified `method`.
If the method is not found in `cls` or any of its ancestor classes, the function returns `None`.

## Purpose 🎯

Intended for scenarios requiring introspection of class hierarchies, such as debugging, dynamic method resolution, or framework development.
It’s also suitable for educational examples of Python’s Method Resolution Order (MRO) and attribute lookup.

## How It Works 🔍

-   **Function Definition**:
    -   Takes two parameters:
        -   `cls`: A class (type) to start the search from.
        -   `method`: A string representing the method name to find.
    -   Returns a `type` (the class defining the method) or `None`.
-   **Implementation**:
    -   Iterates over `cls.__mro__`, which provides the Method Resolution Order (a tuple of classes in the order Python searches for attributes, starting with `cls` and ending with `object`).
    -   For each class `klass` in the MRO, checks if `method` is in `klass.__dict__` (the class’s namespace, which includes methods defined directly in that class).
    -   Returns the first `klass` where `method` is found in `__dict__`.
    -   If no class defines the method, returns `None`.
-   **Behavior**:
    -   Finds the closest class in the inheritance hierarchy that defines the method.
    -   Only considers methods defined directly in a class (not inherited).
    -   Handles single and multiple inheritance correctly via MRO.
    -   Returns `None` for non-existent methods.

## Verification ✅

Implementation satisfies requirements:

-   **Basic Cases**:
    -   Method in class: If `class A: def foo(self): pass`, then `get_method_owner(A, "foo")` → `A`.
    -   Inherited method: If `class B(A): pass`, then `get_method_owner(B, "foo")` → `A`.
    -   Non-existent method: `get_method_owner(A, "bar")` → `None`.
-   **Multiple Inheritance**:
    -   If `class C: def bar(self): pass`, `class D(C, A): pass`, then `get_method_owner(D, "foo")` → `A`, `get_method_owner(D, "bar")` → `C`.
-   **Edge Cases**:
    -   Method in `object`: `get_method_owner(A, "__init__")` → `object` (if not overridden).
    -   Empty class: `class E: pass`, `get_method_owner(E, "foo")` → `None`.
    -   Built-in types: `get_method_owner(int, "__add__")` → `int`.
-   **Correctness**:
    -   Uses `cls.__mro__` to traverse the inheritance hierarchy correctly.
    -   Checks `__dict__` to ensure the method is defined in the class, not inherited.
    -   Returns `None` when the method is not found in the hierarchy.
-   **Documentation**: Clear docstring with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `__mro__` ensures proper handling of single and multiple inheritance.
    -   Checking `__dict__` confirms the method is defined in the class, not inherited.
    -   Returns `None` for non-existent methods, as required.
-   **Performance**:
    -   O(m) where m is the length of the MRO (typically small, as inheritance depth is limited).
    -   `__dict__` lookup is O(1).
    -   Highly efficient for typical class hierarchies.
-   **Design**:
    -   Simple and focused implementation using Python’s built-in introspection.
    -   Type hints (`Union[type, None]`) clarify return type.
    -   Avoids unnecessary complexity (e.g., recursive traversal or attribute access).
-   **Edge Cases**:
    -   Handles built-in types (e.g., `int`, `str`) correctly.
    -   Correctly identifies methods in `object` if not overridden.
    -   No validation needed per requirements (assumes valid `cls` and `method`).

## Usage Example (For Clarity, Not Submission) 📦

```python
# Define test classes
class A:
    def foo(self):
        pass

class B(A):
    def bar(self):
        pass

class C(B):
    pass

# Test cases
print(get_method_owner(A, "foo"))      # <class '__main__.A'>
print(get_method_owner(B, "foo"))      # <class '__main__.A'>
print(get_method_owner(B, "bar"))      # <class '__main__.B'>
print(get_method_owner(C, "foo"))      # <class '__main__.A'>
print(get_method_owner(C, "bar"))      # <class '__main__.B'>
print(get_method_owner(C, "baz"))      # None
print(get_method_owner(int, "__add__")) # <class 'int'>
print(get_method_owner(A, "__init__"))  # <class 'object'>
```

## Conclusion 🚀

The `get_method_owner` function is precise, efficiently finding the class that defines a method in a class’s inheritance hierarchy using MRO.
It’s ideal for introspection tasks or educational examples of Python’s class system, fully compliant with the task’s requirements.

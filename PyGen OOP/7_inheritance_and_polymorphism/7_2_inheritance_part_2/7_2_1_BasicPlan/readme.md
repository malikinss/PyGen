# BasicPlan, SilverPlan, and GoldPlan Class Hierarchy

## Description 📝

The provided code implements three classes: `BasicPlan`, `SilverPlan`, and `GoldPlan`, representing subscription tiers for an online service.
`BasicPlan` defines a basic subscription with specific attributes. `SilverPlan` and `GoldPlan`, subclasses of `BasicPlan`, describe mid-level and high-level subscriptions, respectively, overriding certain attributes.
All classes require no arguments for instantiation and define seven attributes as specified.

## Purpose 🎯

Intended to model subscription plans for online services like streaming platforms, with tiered features and pricing.
The hierarchy is suitable for managing user subscriptions, feature access control, or billing systems, as well as educational examples of inheritance and attribute overriding in Python.

## How It Works 🔍

-   **BasicPlan Class**:
    -   **Initialization**: Takes no arguments (empty `__init__` implicit).
    -   **Attributes** (class-level):
        -   `can_stream = True`
        -   `can_download = True`
        -   `has_SD = True`
        -   `has_HD = False`
        -   `has_UHD = False`
        -   `num_of_devices = 1`
        -   `price = '8.99$'`
-   **SilverPlan Class**:
    -   Inherits from `BasicPlan`, reusing its initialization (no arguments).
    -   **Attributes** (class-level, overriding `BasicPlan`):
        -   `has_HD = True` (overrides `False`)
        -   `num_of_devices = 2` (overrides `1`)
        -   `price = '12.99$'` (overrides `'8.99$'`)
        -   Inherits unchanged: `can_stream = True`, `can_download = True`, `has_SD = True`, `has_UHD = False`.
-   **GoldPlan Class**:
    -   Inherits from `BasicPlan`, reusing its initialization (no arguments).
    -   **Attributes** (class-level, overriding `BasicPlan`):
        -   `has_HD = True` (overrides `False`)
        -   `has_UHD = True` (overrides `False`)
        -   `num_of_devices = 4` (overrides `1`)
        -   `price = '15.99$'` (overrides `'8.99$'`)
        -   Inherits unchanged: `can_stream = True`, `can_download = True`, `has_SD = True`.
-   **Behavior**:
    -   All classes instantiate without arguments.
    -   Attributes are defined at the class level, shared across instances.
    -   Inheritance ensures `SilverPlan` and `GoldPlan` reuse `BasicPlan` attributes unless overridden.

## Verification ✅

Implementation satisfies requirements:

-   **BasicPlan**:
    -   No arguments: `BasicPlan()` creates an instance.
    -   Attributes:
        -   `bp.can_stream` → `True`
        -   `bp.can_download` → `True`
        -   `bp.has_SD` → `True`
        -   `bp.has_HD` → `False`
        -   `bp.has_UHD` → `False`
        -   `bp.num_of_devices` → `1`
        -   `bp.price` → `'8.99$'`
-   **SilverPlan**:
    -   No arguments: `SilverPlan()` creates an instance, same as `BasicPlan`.
    -   Attributes:
        -   `sp.can_stream` → `True` (inherited)
        -   `sp.can_download` → `True` (inherited)
        -   `sp.has_SD` → `True` (inherited)
        -   `sp.has_HD` → `True` (overridden)
        -   `sp.has_UHD` → `False` (inherited)
        -   `sp.num_of_devices` → `2` (overridden)
        -   `sp.price` → `'12.99$'` (overridden)
-   **GoldPlan**:
    -   No arguments: `GoldPlan()` creates an instance, same as `BasicPlan`.
    -   Attributes:
        -   `gp.can_stream` → `True` (inherited)
        -   `gp.can_download` → `True` (inherited)
        -   `gp.has_SD` → `True` (inherited)
        -   `gp.has_HD` → `True` (overridden)
        -   `gp.has_UHD` → `True` (overridden)
        -   `gp.num_of_devices` → `4` (overridden)
        -   `gp.price` → `'15.99$'` (overridden)
-   **Inheritance**:
    -   `issubclass(SilverPlan, BasicPlan)` → `True`
    -   `issubclass(GoldPlan, BasicPlan)` → `True`
-   **Documentation**: Clear docstrings for each class.

## Potential Considerations 🛠️

-   **Correctness**: Attribute values and inheritance match requirements exactly. Class-level attributes are appropriate for shared, immutable plan details.
-   **Extensibility**: Classes can be extended with methods (e.g., `upgrade_plan`) or instance attributes if needed.
-   **Design**: Class-level attributes simplify implementation; inheritance reduces redundancy. Docstrings and type hints enhance clarity.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
bp = BasicPlan()
sp = SilverPlan()
gp = GoldPlan()

# Test attributes
print(bp.has_HD, bp.num_of_devices, bp.price)  # False 1 8.99$
print(sp.has_HD, sp.num_of_devices, sp.price)  # True 2 12.99$
print(gp.has_UHD, gp.num_of_devices, gp.price)  # True 4 15.99$
print(isinstance(gp, BasicPlan))  # True
```

## Conclusion 🚀

The `BasicPlan`, `SilverPlan`, and `GoldPlan` implementation is precise, providing tiered subscription plans with correct attribute values and inheritance.
It’s ideal for subscription-based systems or inheritance education, fully compliant with the task’s requirements.

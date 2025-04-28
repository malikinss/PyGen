# MinStat, MaxStat, and AverageStat Class Implementation

## Description 📝

The provided code implements the `MinStat`, `MaxStat`, and `AverageStat` classes to compute the minimum, maximum, and average of a set of numbers, respectively.
All classes inherit from an abstract base class `Stat`, which centralizes shared logic for storing numbers and implementing common methods (`add`, `clear`, and a generic `result`).
Each class accepts an optional iterable of numbers during instantiation and provides methods to add numbers, compute the statistic, and clear the set.

## Purpose 🎯

Intended for applications requiring simple statistical computations on dynamic sets of numbers, such as data analysis, real-time monitoring, or educational examples of inheritance and abstract base classes in Python.

## Hierarchy Design 🛠️

-   **Why `Stat` as an Abstract Base Class?**:
    -   Centralizes common functionality: storing numbers in a list, implementing `add`, `clear`, and a generic `result` method.
    -   Uses `ABC` to provide a framework for subclasses to define specific statistical computations.
    -   Reduces code duplication by handling list management and empty-set logic once.
-   **Inheritance Structure**:
    -   `MinStat` inherits from `Stat`, implementing `result` to compute the minimum.
    -   `MaxStat` inherits from `Stat`, implementing `result` to compute the maximum.
    -   `AverageStat` inherits from `Stat`, implementing `result` to compute the average.
-   **Why Use a List for Storage?**:
    -   Simple and efficient for dynamic addition and clearing.
    -   Supports all required operations (`min`, `max`, `fmean`) directly.
    -   Ensures independence from the input iterable by copying to `self._numbers`.

## How It Works 🔍

-   **Stat (Abstract Base Class)**:
    -   Initializes with an optional `iterable` (default `()`), storing numbers in `self._numbers` as a list.
    -   `add(num)`: Appends `num` to `self._numbers`.
    -   `clear()`: Clears `self._numbers` using `list.clear`.
    -   `result(action)`: Returns the result of applying `action` (e.g., `min`, `max`, `fmean`) to `self._numbers`, or `None` if empty.
-   **MinStat**:
    -   Inherits from `Stat`.
    -   Implements `result()`: Calls `super().result(min)` to return the minimum value.
-   **MaxStat**:
    -   Inherits from `Stat`.
    -   Implements `result()`: Calls `super().result(max)` to return the maximum value.
-   **AverageStat**:
    -   Inherits from `Stat`.
    -   Implements `result()`: Calls `super().result(fmean)` to return the average using `statistics.fmean`.
-   **Behavior**:
    -   All classes maintain a dynamic set of numbers.
    -   `add` appends numbers, `clear` resets the set, and `result` computes the statistic.
    -   Empty sets return `None` for `result`.
    -   No validation is performed, as inputs are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   `MinStat([1, 2, 3])`, `MaxStat([1, 2, 3])`, `AverageStat([1, 2, 3])` initialize with `[1, 2, 3]`.
    -   `MinStat()` initializes with `[]`.
-   **MinStat Methods**:
    -   `ms = MinStat([1, 2, 3]); ms.result()` → `1`.
    -   `ms.add(0); ms.result()` → `0`.
    -   `ms.clear(); ms.result()` → `None`.
-   **MaxStat Methods**:
    -   `ms = MaxStat([1, 2, 3]); ms.result()` → `3`.
    -   `ms.add(4); ms.result()` → `4`.
    -   `ms.clear(); ms.result()` → `None`.
-   **AverageStat Methods**:
    -   `as = AverageStat([1, 2, 3]); as.result()` → `2.0`.
    -   `as.add(4); as.result()` → `2.5`.
    -   `as.clear(); as.result()` → `None`.
-   **Inheritance**:
    -   `issubclass(MinStat, Stat)` → `True`.
    -   `issubclass(MaxStat, Stat)` → `True`.
    -   `issubclass(AverageStat, Stat)` → `True`.
    -   Shared methods (`add`, `clear`) inherited from `Stat`.
-   **Correctness**:
    -   Uses `list` for storage, ensuring independence from input iterable.
    -   `fmean` provides accurate floating-point averages.
    -   `None` returned for empty sets.
    -   No validation needed per requirements.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `Stat` centralizes list management and empty-set logic, ensuring consistency.
    -   `min`, `max`, and `fmean` correctly compute statistics.
    -   Generic `result(action)` allows flexible statistic computation.
-   **Performance**:
    -   Initialization: O(n) for copying iterable (n is length).
    -   `add`: O(1) amortized for list append.
    -   `clear`: O(1) for list clear.
    -   `result`:
        -   `MinStat`, `MaxStat`: O(n) for `min`, `max`.
        -   `AverageStat`: O(n) for `fmean`.
    -   Efficient for typical use cases with small to medium sets.
-   **Design**:
    -   `Stat` reduces duplication by sharing `add`, `clear`, and `result` logic.
    -   Type hints (`Iterable[Number]`, `float | None`) clarify inputs and outputs.
    -   Simple list storage is sufficient; no need for complex data structures.
    -   `fmean` used for averages to ensure floating-point results.
-   **Alternatives**:
    -   Without `Stat`, `add`, `clear`, and empty-set logic would be duplicated.
    -   Manual average computation (sum/len) is less robust than `fmean`.
    -   Heap-based storage could optimize `MinStat`/`MaxStat` for large sets but adds complexity.
-   **Extensibility**:
    -   Easily extended for other statistics (e.g., median) by adding new subclasses.
    -   Could add validation or optimized storage if needed.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
min_stat = MinStat([1, 2, 3])
max_stat = MaxStat([1, 2, 3])
avg_stat = AverageStat([1, 2, 3])

# Test MinStat
print(min_stat.result())  # 1
min_stat.add(0)
print(min_stat.result())  # 0
min_stat.clear()
print(min_stat.result())  # None

# Test MaxStat
print(max_stat.result())  # 3
max_stat.add(4)
print(max_stat.result())  # 4
max_stat.clear()
print(max_stat.result())  # None

# Test AverageStat
print(avg_stat.result())  # 2.0
avg_stat.add(4)
print(avg_stat.result())  # 2.5
avg_stat.clear()
print(avg_stat.result())  # None
```

## Conclusion 🚀

The `Stat`, `MinStat`, `MaxStat`, and `AverageStat` implementation is precise, providing efficient statistical computations with minimal code duplication.
Using `Stat` as an abstract base class centralizes shared logic, and the design is simple yet extensible.
It’s ideal for statistical tasks or teaching inheritance concepts, fully compliant with the task’s requirements.

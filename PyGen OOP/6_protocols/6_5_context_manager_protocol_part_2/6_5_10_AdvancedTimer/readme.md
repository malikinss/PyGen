# AdvancedTimer Class Execution Time Tracker

## Description 📝

The `AdvancedTimer` class is a reusable context manager that measures the execution time of code within `with` blocks.
It takes no arguments during instantiation and implements the context manager protocol with `__enter__` and `__exit__` methods.
The class maintains four attributes: `last_run` (time of the most recent block), `runs` (list of all block times), `min` (minimum time across blocks), and `max` (maximum time across blocks).
If no measurements have been made, `last_run`, `min`, and `max` are `None`.

## Purpose 🎯

Intended for performance profiling, benchmarking, or debugging where precise timing of code blocks is needed, such as optimizing algorithms, measuring API response times, or comparing function performance.
The reusable nature and detailed statistics make it suitable for iterative testing or educational demonstrations of Python’s context manager protocol and timing utilities.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Sets `self.last_run`, `self.min`, and `self.max` to `None`.
    -   Initializes `self.runs` as an empty list to store execution times.
    -   Sets `self.start` to `None` for tracking block start time.
-   **Enter Method (`__enter__`)**:
    -   Records the start time using `perf_counter()` (high-resolution timer) in `self.start`.
    -   Returns `self`, allowing access to timing attributes within the block.
-   **Exit Method (`__exit__`)**:
    -   Accepts `exc_type`, `exc_value`, and `traceback` for protocol compliance.
    -   Calculates execution time as `perf_counter() - self.start`.
    -   Updates `self.last_run` with the time.
    -   Appends the time to `self.runs`.
    -   If `self.runs` is non-empty, sets `self.min` to `min(self.runs)` and `self.max` to `max(self.runs)`.
-   **Behavior**:
    -   Tracks each `with` block’s duration in seconds.
    -   Maintains a history in `runs` in order of execution.
    -   Updates `min` and `max` dynamically, reflecting all measurements.
    -   Preserves `None` for `last_run`, `min`, and `max` until the first measurement.

## Verification ✅

Implementation satisfies requirements:

-   **Timing**: `with AdvancedTimer() as t: time.sleep(1)` sets `t.last_run` to ~1.0 seconds.
-   **Attributes**:
    -   `runs`: Stores times, e.g., `[1.0, 0.5]` after two blocks.
    -   `min`/`max`: Reflect smallest/largest times, e.g., `0.5`/`1.0`.
    -   `last_run`: Matches the last block’s time.
-   **Initial State**: Before use, `t.last_run`, `t.min`, `t.max` are `None`, `t.runs` is `[]`.
-   **Reusability**: Multiple `with` blocks append to `runs` and update statistics.
-   **Protocol**: `__enter__` and `__exit__` enable `with` statement usage.

## Potential Considerations 🛠️

-   **Accuracy**: `perf_counter()` provides high-precision timing, ideal for benchmarking.
-   **Performance**: Minimal overhead; list operations (`append`, `min`, `max`) are O(n) but negligible for typical use.
-   **Design**: Storing all runs allows flexible statistics; `None` initial state clearly indicates no measurements.

## Usage Example (For Clarity, Not Submission) 📦

```python
timer = AdvancedTimer()
with timer:
    time.sleep(0.5)  # ~0.5s
print(timer.last_run)  # ~0.5
with timer:
    time.sleep(1)  # ~1.0s
print(timer.runs)  # [~0.5, ~1.0]
print(timer.min, timer.max)  # ~0.5 ~1.0
```

## Conclusion 🚀

The `AdvancedTimer` implementation is precise, offering reusable timing with comprehensive statistics.
It’s ideal for performance analysis or protocol education, fully compliant with the task’s requirements.

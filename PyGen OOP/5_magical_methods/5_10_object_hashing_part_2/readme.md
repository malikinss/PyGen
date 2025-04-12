Lesson 5.10: object hashing (part 2)

Hashability and Immutability
Hashing Custom Classes
The **hash**() Magic Method
Hash-Equal Contract

Abstract: The lesson is devoted to hashing objects.

https://stepik.org/lesson/886253/step/1?unit=890908

This lesson has good theory explonation, 2 programing practical tasks and 11 theoretical questions presented on the website.

1. 5_10_1_ColoredPoint

```
# ColoredPoint Class Plane Position Marker
The `ColoredPoint` class represents a point on a 2D plane with `x` and `y` coordinates and a `color` attribute, all set during instantiation.
It provides read-only access to these attributes via properties (`x`, `y`, `color`), ensuring immutability after creation.
The class supports a formal string representation as `ColoredPoint(x, y, 'color')`, equality comparisons (`==`, `!=`) based on matching coordinates and color, and hashing via `hash()` using a tuple of `(x, y, color)`. Invalid comparison operands return `NotImplemented`.
This class is designed for geometric applications, visualization tools, or data structures where points with associated colors need to be uniquely identified, compared, or stored (e.g., in sets or dictionaries).
It’s ideal for graphics programming, game development, or educational exercises demonstrating Python’s property decorators, comparison methods, and hashable objects, offering a clear and robust way to model colored points with consistent behavior.
```

2.

```

```

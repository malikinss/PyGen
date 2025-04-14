Lesson 6.1: iterable objects and iterators protocol

Iterables and iterators
Iterables protocol, **iter**() magic method
Iterators protocol, **next**() magic method
Abstract. The lesson is devoted to the iterables and iterators protocol.

https://stepik.org/lesson/805786/step/1?unit=816645

This lesson has good theory explonation, has 7 programing practical tasks and 12 theoretical questions presented on the website.

1. 6_1_1_Point

```
# Point Class 3D Coordinate Handler
The `Point` class models a point in 3D space, defined by `x`, `y`, and `z` coordinates provided during instantiation.
It offers a formal string representation as `Point(x, y, z)` and implements iterability, allowing the coordinates to be accessed sequentially as an iterable object yielding `x`, `y`, and `z` in that order.
This provides a lightweight and intuitive way to represent and interact with spatial points.
This class is designed for geometric computations, visualization, or simulations requiring 3D points, such as in computer graphics, physics engines, or data analysis.
Its iterable nature makes it convenient for unpacking coordinates or looping through them, while the formal representation aids debugging and logging.
It’s also an excellent educational tool for teaching Python’s special methods, particularly `__repr__` and `__iter__`, in the context of object-oriented programming.

```

2. 6_1_2_DevelopmentTeam

```
# DevelopmentTeam Class Developer Organizer
The `DevelopmentTeam` class models a team of developers categorized into two levels: junior and senior.
It requires no arguments during instantiation and provides two methods, `add_junior` and `add_senior`, to add developers’ names to their respective groups.
The class is iterable, yielding tuples in the format `(name, 'junior')` for junior developers followed by `(name, 'senior')` for senior developers, preserving the order in which they were added.
This structure ensures a clear and sequential representation of the team’s composition.
This class is designed for managing developer teams in software projects, HR systems, or organizational tools, where distinguishing between junior and senior roles is crucial for task allocation, reporting, or team planning.
Its iterable nature simplifies integration into workflows that process team members sequentially, such as generating rosters or assigning tasks.
Additionally, it serves as an educational example for teaching Python’s iterability, list management, and method design, offering a practical illustration of organizing structured data in a class.
```

3. 6_1_3_AttrsIterator

```
# AttrsIterator Class Object Attribute Explorer
The `AttrsIterator` class creates an iterator that traverses the attributes of a given object, yielding each as a tuple containing the attribute name and its value.
It is initialized with a single argument, `obj`, and generates tuples in the order defined by the object’s `__dict__`.
By implementing the iterator protocol with `__iter__` and `__next__`, it ensures seamless integration with Python’s iteration mechanisms, such as for-loops or `next()` calls, providing a structured way to inspect an object’s attributes.
This class is designed for introspecting object attributes in a controlled, sequential manner, making it ideal for debugging, serialization, or dynamic analysis in applications like data processing, object inspection tools, or configuration auditing.
Its iterator-based approach allows efficient attribute access without modifying the source object, and it serves as an educational example for teaching Python’s iterator protocol and dictionary iteration, offering a practical demonstration of custom iterator design.
```

4. 6_1_4_SkipIterator

```
# SkipIterator Class Element Skipper
The `SkipIterator` class creates an iterator that processes an iterable, yielding every `(n+1)`-th element by skipping `n` elements after each yield.
It takes an `iterable` and an integer `n` during initialization, implements the iterator protocol with `__iter__` and `__next__`, and ensures that elements are returned in sequence while respecting the skip count, stopping when the iterable is exhausted.
This class is ideal for sampling data from sequences, such as extracting every nth item from a dataset, filtering large streams, or creating sparse views of lists in applications like data analysis, signal processing, or UI rendering.
It’s also a great educational tool for teaching Python’s iterator protocol and custom iteration logic.
```

5. 6_1_5_RandomLooper

```
# RandomLooper Class Chaotic Element Dispenser
The `RandomLooper` class creates an iterator that randomly yields elements from multiple iterables passed as positional arguments during instantiation.
It implements the iterator protocol with `__iter__` and `__next__`, ensuring that all elements from all iterables are generated in a random order before raising `StopIteration` when exhausted.
The class uses a buffer to store elements and selects them randomly, providing a shuffled traversal across the provided iterables.
This class is designed for scenarios requiring randomized iteration over multiple data sources, such as shuffling combined datasets, random sampling in games, or simulating unpredictable sequences in testing or simulations.
Its ability to intermix elements from different iterables randomly makes it valuable for applications like playlist shuffling, load balancing, or educational exercises demonstrating custom iterators and randomization in Python.
```

6. 6_1_6_Peekable

```
# Peekable Class Enhanced Look-Ahead Iterator
The `Peekable` class implements an iterator that yields elements from a provided iterable in their original order, raising `StopIteration` when exhausted.
It accepts a single `iterable` argument during instantiation and adheres to the iterator protocol with `__iter__` and `__next__`.
The class includes a `peek()` method that previews the next element without advancing the iterator, returning a `default` value if specified when empty, or raising `StopIteration` otherwise.
This version uses a sentinel to distinguish between explicit `None` defaults and no default, offering a nuanced approach to handling exhaustion.
This class is perfect for applications needing to inspect upcoming elements without consuming them, such as in parsers (e.g., lexical analysis), event queues, or data stream processing.
Its lookahead capability enhances control in algorithms like predictive modeling or UI event handling, and it serves as an excellent educational example for Python’s iterator protocol, state management, and sentinel-based default handling in custom iterators.
```

7. 6_1_7_LoopTracker

```
# LoopTracker Class Iteration Monitor
The `LoopTracker` class is an iterator that yields elements from a given iterable in their original order, raising `StopIteration` when exhausted.
It takes a single `iterable` argument during instantiation and tracks iteration statistics through four read-only properties: `accesses` (elements emitted), `empty_accesses` (attempts to access an empty iterator), `first` (first element, or an error if empty), and `last` (last emitted element, or an error if none).
Additionally, it provides an `is_empty()` method to check if the iterator is exhausted.
The class adheres to the iterator protocol with `__iter__` and `__next__`.
This class is designed for scenarios requiring detailed monitoring of iteration, such as debugging data pipelines, profiling iterator usage, or tracking element access in algorithms like streaming or batch processing.
Its properties and method provide insights into the iterator’s state, making it valuable for logging, testing, or educational purposes to illustrate Python’s iterator protocol and stateful iteration.
```

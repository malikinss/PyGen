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

3.

```

```

4.

```

```

5.

```

```

6.

```

```

7.

```

```

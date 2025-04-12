Lesson 5.8: working with object attributes

Attribute Operations
Magic Methods **getattribute**() and **getattr**()
Magic Method **setattr**()
Magic Method **delattr**()

https://stepik.org/lesson/906773/step/1?unit=912312

This lesson has good theory explonation, 8 programing practical tasks and 6 theoretical questions presented on the website.

1. 5_8_1_Item

```
# Item Class Product Descriptor
The `Item` class models a product with attributes for `name`, `price`, and `quantity`, accepting these as arguments during instantiation.
It ensures the `name` attribute is returned with a capital letter (title case) and provides a `total` attribute that computes the product of `price` and `quantity` dynamically.
This implementation corrects an assumed faulty prior version by properly handling attribute access to meet the specified requirements.
This class is designed for inventory or e-commerce scenarios, enabling easy tracking of item details and their total cost.
It’s suitable for retail applications, educational examples of custom attribute access in Python, or any context where products need to be represented with dynamic calculations, such as shopping carts or stock management systems.
```

2. 5_8_2_Logger

```
# Logger Class Attribute Tracker
The `Logger` class is a utility designed to monitor and log modifications to its instance attributes without requiring initialization arguments.
Whenever an attribute is set or updated, it prints a message indicating the attribute name and its new value.
Similarly, when an attribute is deleted, it logs the deletion event with the attribute’s name.
This implementation corrects any prior incorrect attempts by properly handling attribute operations using Python’s special methods.
This class is tailored for debugging, auditing, or tracking changes to object state in Python applications.
It’s ideal for scenarios where developers need visibility into attribute modifications, such as in configuration management, testing environments, or educational settings to illustrate dynamic attribute handling.
Its logging behavior provides a clear audit trail for attribute interactions, enhancing transparency in object lifecycle management.
```

3. 5_8_3_Ord

```
# Ord Class Unicode Accessor
The `Ord` class serves as an alternative interface to Python’s built-in `ord()` function, designed to return the Unicode code point of a single-character attribute name when accessed.
It requires no arguments during instantiation and dynamically handles attribute requests, providing the Unicode value for valid single-character names or raising an `AttributeError` for invalid ones.
This class is crafted for scenarios where accessing Unicode code points via attribute syntax is preferred over function calls, offering a novel way to interact with character encodings.
It’s ideal for educational purposes to demonstrate Python’s dynamic attribute handling, or in specialized applications like text processing, character mapping, or creative coding projects where attribute-based access to Unicode values enhances code expressiveness.
```

4. 5_8_4_DefaultObject

```
# DefaultObject Class Flexible Attribute Handler
The `DefaultObject` class is a dynamic container that accepts a named `default` argument (with a default value of `None`) and any number of additional named arguments during instantiation.
These additional arguments are set as instance attributes, while accessing any non-existent attribute returns the specified `default` value.
This implementation provides a flexible way to create objects with predefined attributes and a fallback for undefined ones.
This class is designed for scenarios requiring objects with customizable attributes and a predictable fallback mechanism, such as configuration management, prototyping, or testing environments.
It’s particularly useful in educational contexts to illustrate Python’s attribute access customization, or in applications like data modeling, where missing attributes should yield a consistent default without raising errors, enhancing robustness and simplicity.
```

5. 5_8_5_NonNegativeObject

```
# NonNegativeObject Class Positive Attribute Setter
The `NonNegativeObject` class is a flexible container that accepts an arbitrary number of named arguments during instantiation, setting them as instance attributes.
For any attribute value that is a negative number (integer or float), it automatically converts it to its positive equivalent by taking the absolute value, while non-numeric or non-negative values are stored unchanged.
This ensures all numeric attributes are non-negative, providing a consistent and predictable object state.
This class is designed for scenarios where objects must maintain non-negative numeric attributes, such as in financial applications (e.g., ensuring positive balances), simulations (e.g., non-negative distances or quantities), or educational exercises demonstrating dynamic attribute manipulation in Python.
Its ability to transparently handle negative inputs makes it valuable for robust data modeling where negative values are invalid or undesirable, simplifying downstream logic.
```

6. 5_8_6_AttrsNumberObject

```
# AttrsNumberObject Class Dynamic Attribute Counter
The `AttrsNumberObject` class is a versatile container that accepts an arbitrary number of named arguments during instantiation, setting them as instance attributes.
It includes a special attribute, `attrs_num`, which dynamically tracks the total number of attributes on the instance, including `attrs_num` itself.
This count updates automatically whenever attributes are added or removed, providing a real-time reflection of the object’s state.
This class is designed for scenarios where tracking the number of attributes on an object is essential, such as in debugging, object introspection, or data modeling with variable attribute sets.
It’s particularly valuable in educational contexts to illustrate Python’s attribute management and dynamic behavior, or in applications like configuration objects, metadata tracking, or flexible data structures where monitoring attribute counts enhances functionality and transparency.
```

7.

```

```

8.

```

```

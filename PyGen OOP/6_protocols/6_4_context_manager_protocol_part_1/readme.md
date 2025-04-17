Lesson 6.4: context manager protocol (part 1)

Context manager protocol
Magic methods **enter**() and **exit**()
Exception handling inside the with block
Examples of using built-in context managers
Examples of creating custom context managers
Abstract. The lesson is devoted to the context manager protocol.

https://stepik.org/lesson/897941/step/1?unit=903008

This lesson has good theory explonation, has 1 programing practical tasks and 22 theoretical questions presented on the website.

6_4_context_manager_protocol_part_1
|\_\_ 6_4_1_is_context_manager

1. 6_4_1_is_context_manager

```
# is_context_manager Function Context Protocol Checker
The `is_context_manager` function accepts an arbitrary object `obj` and returns `True` if it qualifies as a context manager, otherwise `False`.
A context manager is identified by the presence of both `__enter__` and `__exit__` methods, as required by Python’s context management protocol.
Designed for introspection tasks, such as validating objects before use in `with` statements, debugging, or framework development where context manager compatibility must be confirmed.
It’s useful in testing, dynamic type checking, or educational contexts exploring Python’s protocols.
```

Lesson 8.7: Mixins

Mixins
Mixin usage scenarios
Mixin usage issues
Abstract. The lesson is dedicated to mixins in Python.

https://stepik.org/lesson/1525202/step/1?unit=1545578

This lesson has good theory explonation, has 4 programing practical tasks and 8 theoretical questions presented on the website.

1. 8_7_1_JsonSerializableMixin

```
# JsonSerializableMixin Class Implementation

## Description 📝

The provided code implements the `JsonSerializableMixin` class, a mixin that adds JSON serialization functionality to classes.
It defines a single method, `to_json()`, which returns a JSON-formatted string by serializing the instance’s attribute dictionary using `json.dumps`.
The implementation is simple, leveraging Python’s `json` module to handle serialization and the instance’s `__dict__` to access attributes.

## Purpose 🎯

Intended for applications requiring JSON serialization of class instances, such as API development, data interchange, or educational examples of Python mixins, JSON handling, and instance attribute serialization.
```

2. 8_7_2_LoggerMixin

```
# LoggerMixin Class Implementation

## Description 📝

The provided code implements the `LoggerMixin` class, a mixin that adds logging functionality to classes.
It defines a single method, `log()`, which takes a logging level and message as arguments and prints a formatted log entry.
The log entry includes the current date and time in `DD.MM.YYYY HH:MM:SS` format, the logging level, the class name, and the message, following the specified format: `[<date and time>] - <level> - <class name>: <message>`.

## Purpose 🎯

Intended for applications requiring logging capabilities, such as debugging, event tracking, or educational examples of Python mixins, datetime formatting, and class-based logging.
```

3.

```

```

4.

```

```

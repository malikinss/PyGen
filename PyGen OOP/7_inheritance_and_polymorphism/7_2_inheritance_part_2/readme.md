Lesson 7.2: inheritance (part 2)

Overriding Methods
Extending Methods
The super() Function
Using Descendant Methods in a Base Class
Abstract: This lesson is about inheritance in Python.

https://stepik.org/lesson/798678/step/1?unit=801641

This lesson has good theory explonation, has 6 programing practical tasks and 14 theoretical questions presented on the website.

1. 7_2_1_BasicPlan

```
# BasicPlan, SilverPlan, and GoldPlan Class Hierarchy

## Description 📝

The provided code implements three classes: `BasicPlan`, `SilverPlan`, and `GoldPlan`, representing subscription tiers for an online service.
`BasicPlan` defines a basic subscription with specific attributes. `SilverPlan` and `GoldPlan`, subclasses of `BasicPlan`, describe mid-level and high-level subscriptions, respectively, overriding certain attributes.
All classes require no arguments for instantiation and define seven attributes as specified.

## Purpose 🎯

Intended to model subscription plans for online services like streaming platforms, with tiered features and pricing.
The hierarchy is suitable for managing user subscriptions, feature access control, or billing systems, as well as educational examples of inheritance and attribute overriding in Python.
```

2. 7_2_2_WeatherWarning

```
# WeatherWarning and WeatherWarningWithDate Class Hierarchy

## Description 📝

The provided code implements two classes: `WeatherWarning` and `WeatherWarningWithDate`.
The `WeatherWarning` class represents a weather warning system with three methods (`rain`, `snow`, `low_temperature`) that print specific weather alerts.
It requires no arguments for instantiation. The `WeatherWarningWithDate` class, a subclass of `WeatherWarning`, extends the warning system to include a date, with overridden methods that accept a `date` object and prepend the date in `DD.MM.YYYY` format to the warnings.
Both classes instantiate without arguments.

## Purpose 🎯

Intended to model a weather alert system for applications like weather forecasting apps, emergency notifications, or environmental monitoring tools.
The hierarchy allows basic and date-specific warnings, suitable for extensible warning systems or educational examples of inheritance and method overriding in Python.
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

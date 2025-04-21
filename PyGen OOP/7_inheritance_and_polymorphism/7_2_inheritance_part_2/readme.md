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

3. 7_2_3_Triangle

```
# Triangle and EquilateralTriangle Class Hierarchy

## Description 📝

The provided code implements two classes: `Triangle` and `EquilateralTriangle`.
The `Triangle` class represents a general triangle, initialized with three side lengths (`a`, `b`, `c`) and featuring a `perimeter` method that returns the sum of the sides.
The `EquilateralTriangle` class, a subclass of `Triangle`, represents an equilateral triangle, initialized with a single `side` length, which is used for all three sides.

## Purpose 🎯

Intended to model triangles in geometric applications, such as graphics, physics simulations, or mathematical tools.
The hierarchy supports general and specialized triangle types, making it suitable for extensible geometric modeling or educational examples of inheritance and method reuse in Python.
```

4. 7_2_4_Counter

```
# DoubledCounter Class Implementation

## Description 📝

The provided code implements the `DoubledCounter` class, a subclass of the given `Counter` class.
The `Counter` class represents a non-negative counter with a `value` attribute and methods `inc` and `dec` to increment or decrement the counter, ensuring non-negativity.
The `DoubledCounter` class extends `Counter` to double the effect of incrementing and decrementing operations, while maintaining the same initialization process and non-negative constraint.

## Purpose 🎯

Intended to model a counter with amplified increment and decrement operations, suitable for applications requiring scaled counting, such as tracking events with weighted impacts or simulations.
It’s also ideal for educational examples of inheritance and method overriding in Python.
```

5. 7_2_5_Summator

```
# Summator Class Hierarchy

## Description 📝

The provided code implements four classes: `Summator`, `SquareSummator`, `QubeSummator`, and `CustomSummator`.
The `Summator` class calculates the sum of natural numbers from 1 to `n` (1 + 2 + ... + n) using a `total` method.
Its subclasses—`SquareSummator` (sum of squares: 1² + 2² + ... + n²), `QubeSummator` (sum of cubes: 1³ + 2³ + ... + n³), and `CustomSummator` (sum of m-th powers: 1^m + 2^m + ... + n^m)—extend this functionality by overriding the power used in the calculation.
The `total` method is defined only in `Summator`, reused by all subclasses via a `power` attribute.

## Purpose 🎯

Intended to model mathematical summation operations for natural numbers raised to specific or custom powers, suitable for mathematical computations, data analysis, or algorithm development.
The hierarchy demonstrates inheritance and method reuse, making it ideal for extensible calculation frameworks or educational examples of object-oriented programming in Python.
```

6.

```

```

# User Subscription Plan Sorting 📝

## Description 📝

This program processes a list of `User` named tuples, where each tuple holds data about a user:
their first name, last name, email, and subscription plan.
The program sorts the users first by subscription plan (from most expensive to cheapest), and in case of ties, by email address in lexicographic order.
The user data is then printed in a readable format.

## Purpose 🎯

The purpose of this program is to:

-   Sort a list of users by their subscription status in descending order (Gold, Silver, Bronze, Basic).
-   If two users have the same subscription plan, sort them by email address in lexicographic order.
-   Display the sorted user data in a specified format.

## Output 📜

The output consists of user details displayed as:

-   Full name (first name and last name)
-   Email address
-   Subscription plan
    An empty line is inserted between each user's details.

## Usage 📦

To use the program, simply run the script after ensuring that the `users` list is defined with valid `User` namedtuples.

### Example:

```bash
$ python user_subscription_sort.py
```

### Expected Output (based on the example input)

```
Kathleen Lyons
  Email: balchen@att.net
  Plan: Gold

William Townsend
  Email: kosact@verizon.net
  Plan: Gold

Brenda Young
  Email: retoh@outlook.com
  Plan: Silver

Pamela Hicks
  Email: corrada@sbcglobal.net
  Plan: Silver

Mary Griffin
  Email: sonnen@yahoo.com
  Plan: Basic
```

## Conclusion 🚀

This program effectively sorts users based on their subscription plans and email addresses, ensuring the data is displayed in a readable and organized format.

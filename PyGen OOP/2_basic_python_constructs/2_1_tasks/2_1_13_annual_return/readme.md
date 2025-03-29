# Annual Return Generator Function ⚙️

## Description 📝

The `annual_return()` function simulates a bank deposit that grows over time based on an annual interest rate. Each year, the deposit increases by the specified percentage, and the function yields the updated deposit amount after the interest is accrued.

## Purpose 🎯

This function is designed to model the growth of an investment (such as a bank deposit) over a period of years.
It simulates the effect of compound interest by updating the deposit each year and returning the new deposit value.

## How It Works 🔍

1. The function takes three arguments:
    - `start`: The initial deposit amount (in rubles).
    - `percent`: The annual interest rate (as a percentage).
    - `years`: The number of years over which the interest will be applied.
2. The function uses a generator pattern to yield the deposit amount after each year, with the interest applied each time.
3. For each year, the deposit amount is increased by the specified percentage (i.e., the deposit is multiplied by `(1 + percent / 100)`).
4. The updated deposit value is rounded to two decimal places before being yielded.

### Example Inputs & Outputs:

| Input                               | Output                   |
| ----------------------------------- | ------------------------ |
| `start=120000, percent=10, years=3` | `132000, 145200, 159720` |
| `start=1000, percent=5, years=2`    | `1050, 1102.5`           |

## Output 📜

The function yields the deposit amount after interest is accrued for each year.

## Usage 📦

1. Call `annual_return()` with the initial deposit, interest rate, and number of years.
2. Iterate over the result to get the deposit amount for each year.

## Conclusion 🚀

The `annual_return()` generator is a useful tool for simulating the growth of a deposit over time with interest.
It's a simple way to model the effect of compound interest in financial scenarios.

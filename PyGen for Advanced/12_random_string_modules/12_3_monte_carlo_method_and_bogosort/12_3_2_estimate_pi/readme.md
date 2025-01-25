# Monte Carlo π Approximation

## Description 📝

This program estimates the value of π using the Monte Carlo method.
By leveraging random sampling, it calculates the ratio of points that fall inside a unit circle to the total number of points in a bounding square, which corresponds to the approximate value of π.

## Purpose 🎯

The program demonstrates how the Monte Carlo method can be applied to approximate mathematical constants.
It is a practical example of probability-based numerical estimation techniques.

## How It Works 🔍

1. **Unit Circle:** A circle with radius \(R = 1\) centered at the origin \((0, 0)\). Its area is \(S = πR^2 = π\).
2. **Bounding Square:** The square enclosing the unit circle spans \([-1, 1] \times [-1, 1]\) and has an area of \(4\).
3. **Random Sampling:**
    - Generate random points \((x, y)\) within the bounding square.
    - Check if each point lies inside the unit circle using the equation \(x^2 + y^2 \leq 1\).
4. **π Approximation:**
   \[
   \pi \approx 4 \times \left(\frac{\text{Points Inside Circle}}{\text{Total Points}}\right)
   \]

## Output 📜

The program outputs the estimated value of π. Example output:

```
Estimated value of π: 3.141592
```

## Usage 📦

1. Set the number of Monte Carlo trials (`trials`) for the approximation.
2. Run the program to observe the estimated value of π.

### Example:

```python
trials = 10**6  # Number of random points
```

**Run the program:**

```bash
python monte_carlo_pi.py
```

**Output:**

```
Estimated value of π: 3.141592
```

## Conclusion 🚀

This program provides an efficient and probabilistic way to approximate π using the Monte Carlo method.
Increasing the number of trials improves accuracy, demonstrating the power of random sampling in numerical estimation.

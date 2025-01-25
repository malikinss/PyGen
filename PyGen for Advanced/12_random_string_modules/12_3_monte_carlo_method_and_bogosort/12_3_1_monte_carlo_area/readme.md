# Monte Carlo Area Calculation of a Figure

## Description 📝

This program uses the Monte Carlo method to estimate the area of a figure defined by a system of inequalities.
The bounding rectangle is defined within the range \([-2, 2]\) for both \(x\) and \(y\).
The figure satisfies the following inequalities:

\[
\begin{aligned}
&-2 \leq x \leq 2, \\
&-2 \leq y \leq 2, \\
&x^3 + y^4 + 2 \geq 0, \\
&3x + y^2 \leq 2.
\end{aligned}
\]

## Purpose 🎯

This program demonstrates how to apply the Monte Carlo method to estimate the area of complex geometrical shapes defined by inequalities.
It is a practical example of using random sampling for numerical approximations.

## How It Works 🔍

1. **Bounding Rectangle:** The figure is bounded within the square \([-2, 2] \times [-2, 2]\), with an area of \(16\).
2. **Random Sampling:** The program generates a specified number of random points (\(x, y\)) within the bounding rectangle.
3. **Figure Inclusion:** For each point, it checks whether the point lies inside the figure based on the given inequalities.
4. **Area Estimation:** The area of the figure is estimated as:
   \[
   \text{Area} = \left( \frac{\text{Points Inside}}{\text{Total Points}} \right) \times \text{Bounding Area}
   \]

## Output 📜

The program outputs the estimated area of the figure. Example output:

```
Estimated area of the figure: 8.123456
```

## Usage 📦

1. Run the program.
2. Set the number of Monte Carlo trials (`trials`) to control the accuracy of the estimation.
3. Observe the calculated area.

### Example:

```bash
trials = 10**6  # Number of random points
bounding_area = 16  # Area of the bounding rectangle
```

**Run the program:**

```bash
Estimated area of the figure: 8.123456
```

## Conclusion 🚀

This program provides an efficient way to estimate the area of a figure using the Monte Carlo method.
By increasing the number of trials, you can achieve higher accuracy.
It's a practical application of probability and numerical methods for solving geometrical problems.

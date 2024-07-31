import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

def f(x: float) -> float:
    """
    Define the function to be integrated

    :param x: float
    :return: float
    """
    return x ** 2

# Limits of integration
a = 0
b = 2

# Estimate the integral using Monte Carlo method
N = 10000  # Number of random points
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)
under_curve = y_random < f(x_random)
area_estimate = np.mean(under_curve) * (b - a) * f(b)

# Calculate the integral using the quad function
result, error = spi.quad(f, a, b)

# Print the results
print("Значення інтегралу за методом Монте-Карло:", area_estimate)
print("Точне значення інтегралу:", result)
print("Абсолютна помилка:", error)

# Plot the function and the area under the curve
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)  # Graph of the function
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)  # Area under the curve
ax.scatter(x_random[under_curve], y_random[under_curve], color='green', s=1, alpha=0.5)  # Green points under the curve
ax.scatter(x_random[~under_curve], y_random[~under_curve], color='red', s=1, alpha=0.5)  # Red points above the curve
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

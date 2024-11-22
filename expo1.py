#exponential distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
scales = [1, 1.5, 2]
x = np.linspace(0, 10, 500)
plt.figure(figsize=(4, 3))
for scale in scales:
    y = expon.pdf(x, scale=scale)
    plt.plot(x, y, label=f'scale={scale}')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Exponential Distribution')
plt.legend()
plt.grid(True)
plt.show()

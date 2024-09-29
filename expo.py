#exponential distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
scale = 3 # This is 1/lambda (lambda is the rate parameter)
x = np.linspace(0, 6)
# Calculating the exponential probability distribution
y = expon.pdf(x, scale=scale)
plt.figure(figsize=(5, 3))
plt.plot(x, y, 'b-', label='expon pdf')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Exponential Distribution (scale=3)')
plt.legend()
plt.grid(True)
plt.show()

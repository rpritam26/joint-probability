#binomial distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
n = 8
p = 0.3
x = np.arange(0, n+1)
y = binom.pmf(x, n, p)
plt.figure(figsize=(5, 3))
plt.stem(x, y)
plt.xlabel('Number of Success')
plt.ylabel('Probability')
plt.title('Binomial Distribution (n=8, p=0.3)')
plt.grid(True)
plt.show()

#bernoulli distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
p = 0.2
x = np.array([0,1])
# Calculating the Bernoulli probability distribution
y = bernoulli.pmf(x, p)
# Plotting the Bernoulli distribution
plt.figure(figsize=(4, 2.5))
plt.bar(x, y, width=0.1, color='red')
plt.xticks(x)
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.title('Bernoulli Distribution(p=0.2)')
plt.grid(True)
plt.show()

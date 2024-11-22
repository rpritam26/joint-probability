#normal distributions
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
means = [90, 90, 90]
std_devs = [20, 30, 35]
x_data = np.arange(0, 200, 0.01)
plt.figure(figsize=(10, 6))
for mean, std_dev in zip(means, std_devs):
    y_data = stats.norm.pdf(x_data, mean, std_dev)
    plt.plot(x_data, y_data, label=f'mean={mean}, std={std_dev}')
plt.title('Multiple Normal Distributions')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()
plt.show()

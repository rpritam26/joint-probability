import matplotlib.pyplot as plt
import numpy as np
# Generate random numbers
points = 25  # Number of random points
random_numbers = np.random.rand(points)
# Plot the random numbers
plt.figure(figsize=(4, 3))
plt.plot(random_numbers, marker='o',color='g')
plt.title('Random Numbers')
plt.xlabel('Index')
plt.ylabel('Random Value')
plt.show()

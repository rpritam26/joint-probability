import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.stats as stats
def plot_bivariate_normal(mean, cov):
    x = np.linspace(-3, 3, 100)
    y = np.linspace(0, 3, 100)
    X, Y = np.meshgrid(x, y)
    pos = np.dstack((X, Y))
    Z = stats.multivariate_normal(mean, cov).pdf(pos)
    
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plt.contourf(X, Y, Z, cmap='magma')
    plt.colorbar()
    plt.title('Bivariate Normal Distribution (Contour Plot)')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    ax = plt.subplot(1, 2, 2, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='magma', edgecolor='none')
    ax.set_title('Bivariate Normal Distribution (3D Surface Plot)')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Density')

    plt.tight_layout()
    plt.show()

# Example Usage
mean = [0, 0]  # Mean vector
cov = [[1, 0.5], [0.5, 1]]  # Covariance matrix

# Plotting Bivariate Normal Distribution
plot_bivariate_normal(mean, cov)

#normal distribution
pip install matplotlib
import numpy as np 
import scipy as sp 
from scipy import stats 
import matplotlib.pyplot as plt  
x_data = np.arange(0, 2000,0.01) 
y_data = stats.norm.pdf(x_data, 1100,300) 
plt.figure(figsize=(6, 4))
plt.plot(x_data, y_data)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x_axis_Bob = np.arange(80, 120, 0.000001)
x_axis_Clare = np.arange(80, 120, 0.00001)

plt.plot(x_axis_Bob, norm.pdf(x_axis_Bob,100,5), label='Bob')
plt.plot(x_axis_Clare, norm.pdf(x_axis_Clare,100,10), label='Clare')
plt.legend(loc='upper left')
plt.show()
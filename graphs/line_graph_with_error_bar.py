import matplotlib.pyplot as plt
import numpy as np

#sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])
z = np.array([0.1, 0.4, 0.19, 0.16, 0.25])

plt.errorbar(x, y, yerr=z, fmt="-o", capsize=5, label="data 1")
plt.title('Sample Line Graph')
plt.xlabel('Data')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
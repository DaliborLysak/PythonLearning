import matplotlib.pyplot as plt
import numpy as np

#sample data
x = np.random.randn(1000)
y = np.random.randn(1000)

plt.hist2d(x, y, bins=30, cmap='plasma')
plt.colorbar(label='Counts')
plt.title('2D Histogram')
plt.xlabel('Data')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
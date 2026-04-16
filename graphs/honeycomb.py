import matplotlib.pyplot as plt
import numpy as np

x=np.random.rand(10000)
y=np.random.rand(10000)

plt.hexbin(x, y, gridsize=30, cmap='Blues', edgecolors='grey')
plt.colorbar(label='Counts')

plt.title('Honeycomb Plot')
plt.xlabel('Data')  
plt.ylabel('Value')
plt.grid(True)

plt.show()
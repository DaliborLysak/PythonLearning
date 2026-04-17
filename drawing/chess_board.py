import numpy as np
import matplotlib.pyplot as plt

board = np.indices((8, 8)).sum(axis=0) % 2
plt.figure(figsize=(6, 6))
plt.imshow(board, cmap='gray', interpolation="nearest")
plt.xticks([])
plt.yticks([])
plt.title('Chess Board')
plt.show()
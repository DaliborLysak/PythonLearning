import numpy as np
import matplotlib.pyplot as plt

radius = 1
num_points = 50
theta = np.linspace(0, 2 * np.pi, num_points)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
fig, ax = plt.subplots()

ax.scatter(x, y, color ='black', s=50)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

ax.set_aspect('equal', adjustable='box')
# ax.axis('off')
plt.title('Circle Shape')

plt.show()
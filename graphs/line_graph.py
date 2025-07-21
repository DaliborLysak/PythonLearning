import matplotlib.pyplot as plt

#sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
z = [1, 4, 9, 16, 25]

plt.plot(x, y, label="data 1", marker="o")
plt.plot(x, z, label="data 1", marker="s")
plt.title('Sample Line Graph')
plt.xlabel('Data')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
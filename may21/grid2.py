import matplotlib.pyplot as plt

points = [
    (0, 10),
    (10, 20),
    (20, 40),
    (60, 100),
]

x = list(map(lambda x: x[0], points))
y = list(map(lambda x: x[1], points))

plt.scatter(x, y)
plt.grid(True)

plt.show()
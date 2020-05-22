import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(10))
y = 5*x+3

# Create the plot
plt.plot(x,y,label='y = 5*x+3')
plt.plot(x, y- 5*x + x**2,label='y =x^2+3 ')


# Add a title
plt.title('My first Plot with Python')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=.4,linestyle='--')
plt.legend()
plt.show()

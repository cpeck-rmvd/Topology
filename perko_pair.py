import matplotlib.pyplot as plt
import numpy as np

# Define the Perko pair function
def perko_pair(x, y):
    return np.sin(x) - np.cos(y), np.cos(x) + np.sin(y)

# Generate a grid of points to display
x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(x, y)

# Compute the Perko pair for each point
U, V = perko_pair(X, Y)

# Display the Perko pair using quiver
plt.figure()
plt.quiver(X, Y, U, V)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Define the parameter for the trefoil knot
r = 3

# Create a set of points for the trefoil knot
t = np.linspace(0, 2*np.pi, 1000)
x = r * np.cos(t) + r * np.cos(2*t)
y = r * np.sin(t) - r * np.sin(2*t)
z = -np.sin(3*t)

# Create and show the trefoil knot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Create a set of points for the figure 8 knot
t = np.linspace(0, 2*np.pi, 1000)
x = (2 + np.cos(2*t))*np.cos(t)
y = (2 + np.cos(2*t))*np.sin(t)
z = np.sin(2*t)

# Create and show the figure 8 knot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
plt.show()

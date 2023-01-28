import numpy as np
import matplotlib.pyplot as plt

# Define the parameter for the Cinquefoil knot
p = 5

# Create a set of points for the Cinquefoil knot
t = np.linspace(0, 2*np.pi, 1000)
x = np.cos(2 * t) * (3 + np.cos(p * t))
y = np.sin(2 * t) * (3 + np.cos(p * t))
z = np.sin(p * t)

# Graph the Cinquefoil knot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
plt.show()

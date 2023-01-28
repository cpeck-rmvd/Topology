import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the pretzel knot
p = 2
q = 3
r = -4

# Create a set of points for the pretzel knot
t = np.linspace(0, 2*np.pi, 1000)
x = np.sin(p * t) * np.cos(q * t + r)
y = np.sin(p * t) * np.sin(q * t + r)
z = np.cos(p * t)

# Create and show the pretzel knot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
plt.show()

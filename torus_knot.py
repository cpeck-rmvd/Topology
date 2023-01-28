import numpy as np
import matplotlib.pyplot as plt

# Define the parameter for the torus knot
p = 3
q = 4

# Create a set of points for the torus knot
t = np.linspace(0, 2*np.pi, 100)
x = (1 + 0.3*np.cos(q*t)) * np.cos(p*t)
y = (1 + 0.3*np.cos(q*t)) * np.sin(p*t)
z = 0.3 * np.sin(q*t)

# Graph the torus knot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
plt.show()

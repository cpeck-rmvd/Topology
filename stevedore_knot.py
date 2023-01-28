import matplotlib.pyplot as plt

# Define the Stevedore knot function
def stevedore_knot(t):
    x = (2 + np.cos(3 * t)) * np.cos(2 * t)
    y = (2 + np.cos(3 * t)) * np.sin(2 * t)
    return x, y

# Generate a set of points on the Stevedore knot
t = np.linspace(0, 2 * np.pi, 1000)
x, y = stevedore_knot(t)

# Display the Stevedore knot
plt.figure()
plt.plot(x, y)
plt.show()

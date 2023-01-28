import numpy as np
from scipy.spatial import ConvexHull
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# create a knot
knot = ConvexHull(np.random.rand(30, 3))

# plot knot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(knot.points[:,0], knot.points[:,1], knot.points[:,2],
                triangles=knot.simplices)
plt.show()

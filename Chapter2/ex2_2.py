import matplotlib.pyplot as plt
import numpy as np

"""Counter plot and Surface plot for comparison"""

x1 = x2 = np.linspace(-100, 100, 20)

X, Y = np.meshgrid(x1, x2)

Z = 8 * X + 12 * Y + np.power(X, 2) - 2 * np.power(Y, 2)

plt.figure()
cp = plt.contour(X, Y, Z)
plt.clabel(cp, inline=True,
          fontsize=10)
plt.title('Contour Plot')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

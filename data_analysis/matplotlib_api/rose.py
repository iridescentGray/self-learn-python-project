import math

import matplotlib.pyplot as plt
import numpy as np

n = 800
A = 1.995653
B = 1.27689
C = 8

r = np.linspace(0, 1, n)

theta = np.linspace(-2, 20 * math.pi, n)

[R, THETA] = np.meshgrid(r, theta)

petalNum = 3.6
x = (
    1
    - (1 / 2)
    * ((5 / 4) * (1 - np.mod(petalNum * THETA, 2 * math.pi) / math.pi) ** 2 - 1 / 4)
    ** 2
)
phi = (math.pi / 2) * np.exp(-THETA / (C * math.pi))
y = A * (R**2) * ((B * R - 1) ** 2) * np.sin(phi)
R2 = x * (R * np.sin(phi) + y * np.cos(phi))
X = R2 * np.sin(THETA)
Y = R2 * np.cos(THETA)
Z = x * (R * np.cos(phi) - y * np.sin(phi))

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, rstride=6, cstride=6, cmap="Reds", antialiased=True, alpha=1)
plt.show()

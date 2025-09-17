"""
Create a 3D function plot for visualizing continuous optimization.

This one is based on the MatplotLib example given at
https://matplotlib.org/stable/gallery/mplot3d/surface3d.html
visited on 2025-09-16

However, we **massively** changed the way the data is generated
and shown.

The original file has the following copyright information:
Copyright 2002-2012 John Hunter, Darren Dale, Eric Firing,
Michael Droettboom and the Matplotlib development team;
2012-2025 The Matplotlib development team.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

width = 6.4
height = 4.8
fig, ax = plt.subplots(subplot_kw={"projection": "3d"},
                       figsize=[width, height])

# Make data.
# This part is massively changed.
MAX = 18
X = np.arange(-MAX, MAX, 0.0025 * MAX)
Y = np.arange(-MAX, MAX, 0.0025 * MAX)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R) * np.exp(-0.1*R)

for x, y, h in ((0.1*MAX, 0.4*MAX, 0.5), (-0.2*MAX, -0.8*MAX, -0.3),
                (0.5*MAX, -0.2*MAX, 0.6), (0.6*MAX, 0.7*MAX, 0.3)):
    R = np.sqrt( (X - x)**2 + (Y - y)**2 )
    R = np.abs(max(R.flatten()) - R) ** 3
    R = (R / max(R.flatten())) * h
    Z += R

R = np.sqrt(X**2 + Y**2)
Z = Z + (-max(Z.flatten())) + 0.05*R**1.1

min_idx = np.argmin(Z.flatten())
min_x = X.flatten()[min_idx]
min_y = Y.flatten()[min_idx]
min_z = Z.flatten()[min_idx]
max_z = max(Z.flatten())
print(f"Minima are x={min_x}, y={min_y}, z={min_z}")


# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm_r,#cm.cool_r,
                       linewidth=0, antialiased=True)

# Customize the z axis.
ax.set_zlim(1.01 * min(Z.flatten()), 1.01 * max(Z.flatten()))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter("{x:.02f}")

# This is also added by us.
fig.savefig(
    "./function3d.pdf", transparent=True, format="pdf",
    orientation="landscape",
    dpi="figure",
    bbox_inches="tight",
    pad_inches=1.0 / 72.0)

# Locate Minimum
ax.scatter(min_y, min_x, min_z - 0.02*(max_z - min_z), color="red",
           marker="o")
z_base =  min_z - 0.02*(max_z - min_z)
ax.plot( (min_x, min_x), (min(Y.flatten()), max(Y.flatten())),
         (z_base, z_base), color="red")
ax.plot( (min(X.flatten()), max(X.flatten())), (min_y, min_y),
         (z_base, z_base), color="red")

# This is also added by us.
fig.savefig(
    "./function3d_optimum.pdf", transparent=True, format="pdf",
    orientation="landscape",
    dpi="figure",
    bbox_inches="tight",
    pad_inches=1.0 / 72.0)

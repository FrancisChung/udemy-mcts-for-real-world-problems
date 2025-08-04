# Libraries Imported

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
a =2                            # radius and side length of the square
circle_center = (4*a, 0)

square_bottom_left = (0, -a/2)

num_point = 3000

# Setup Figures
fig, ax = plt.subplots(figsize=(10,5))
ax.set_xlim(-a, 6*a)
ax.set_ylim(-1.5*a, 1.5*a)
ax.set_aspect('equal')
ax.set_title('Monte Carlo Simulation')

# Draw Square
square = plt. Rectangle(square_bottom_left, a, a, edgecolor = 'green', facecolor = 'none', linewidth = 2, label = 'Square')
ax.Add_patch(square)

# Draw Circle
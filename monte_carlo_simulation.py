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
circle = plt.Circle(circle_center, a, facecolor = 'none', edgecolor = 'blue', linewidth = 2,  label = 'Circle')
ax.Add_patch(circle)

# Legend
ax.legend(loc = 'upper right')

# Scatter plots for points
points_circle = ax.plot([], [], 'o', color = 'blue', markersize = 4, label = 'Points in Circle')
points_square = ax.plot([], [], 'o', color = 'green', markersize = 4, label = 'Points in Square')
points_other = ax.plot([], [], 'o', color = 'gray', markersize = 4, label = 'Points Outside')

# Text for Ratio
text_ratio =  ax.text (0,5, 1.1, '', transform = ax.transAxes, fontsize = 12, ha = 'center', verticalalignment = 'top',
                       bbox = dict(facecolor = 'white', alpha = 0.7))

# Main Code


# Counters
count_in_circle = 0
count_in_square = 0


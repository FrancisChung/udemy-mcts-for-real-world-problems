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

# Initialize lists to store
points_in_circle_x = []
points_in_circle_y = []
points_in_square_x = []
points_in_square_y = []
points_in_other_x = []
points_in_other_y = []



def animate(i):
    global count_in_circle, count_in_square

    #generate random points
    x = np.random.uniform(-a, 6*a)
    y = np.random.uniform(-1.5*a, 1.5*a)

    in_circle = False
    in_square = False

    # Check for circle
    if (x - circle_center[0]) ** 2 + (y - circle_center[1]) ** 2 <= a ** 2:
        count_in_circle += 1
        points_in_circle_x.append(x)
        points_in_circle_y.append(y)
        in_circle = True

    # Check for square
    if ((square_bottom_left[0] <= x <= square_bottom_left[0] + a) and
        (square_bottom_left[1] <= y <= square_bottom_left[1] + a)) :

        count_in_square += 1
        points_in_square_x.append(x)
        points_in_square_y.append(y)
        in_square = True

    # Update Scatter Plot
    points_circle.set_data(points_in_circle_x, points_in_circle_y)
    points_square.set_data(points_in_square_x, points_in_square_y)

    # other points
    if not in_circle and not in_square:
        points_in_other_x.append(x)
        points_in_other_y.append(y)
        points_other.set_data(points_in_other_x, points_in_other_y)

    # calculate ratio
    if count_in_square > 0:
        ratio = count_in_circle / count_in_square
        text_ratio.set_text(f'Ratio (Circle / Square): {ratio:.5f}')
    else:
        text_ratio.set_text('Calculating...')

    return points_circle, points_square, points_other, text_ratio

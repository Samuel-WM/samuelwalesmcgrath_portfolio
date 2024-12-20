import matplotlib.pyplot as plt
import numpy as np

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))

# Define the triangular region
x = np.linspace(0, 2, 500)
y1 = x  # Line y = x
y2 = np.full_like(x, 2)  # Line y = 2

# Fill regions
# Region 1: y from x to 2
x1 = np.linspace(0, 2, 500)
y1_lower = x1
y1_upper = 2
ax.fill_between(x1, y1_lower, y1_upper, color='lightblue', alpha=0.5, label='Region 1 (y >= x)')

# Region 2: x from 0 to y
y2_vals = np.linspace(0, 2, 500)
x2_lower = 0
x2_upper = y2_vals
for y_val in y2_vals:
    ax.fill_betweenx(y_val, x2_lower, x2_upper, color='lightgreen', alpha=0.5, label='Region 2 (y <= x)' if y_val == y2_vals[0] else "")

# Add boundary lines
ax.plot(x, y1, 'b-', label='y = x', linewidth=2)
ax.plot(x, y2, 'k-', label='y = 2', linewidth=2)

# Add labels and legend
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('Regions of Integration', fontsize=16)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.legend()
ax.grid(True, linestyle='--', alpha=0.7)

plt.show()

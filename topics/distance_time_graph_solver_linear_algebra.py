import numpy as np
import matplotlib.pyplot as plt

# Time range and distances
t = np.linspace(0, 1000, 1000)  # start, finish, n points
d_r = 2.5 * t  # Distance of the robber
d_s = 3 * (t - 5)  # Distance of the sheriff

# Create the figure and axis
fig, ax = plt.subplots()
plt.title('A Bank Robber Caught')  # Title of the plot
plt.xlabel('time (in minutes)')    # X-axis label
plt.ylabel('distance (in km)')     # Y-axis label

# Set axis limits
ax.set_xlim([0, 40])
ax.set_ylim([0, 100])

# Plot the distances
ax.plot(t, d_r, c='green', label='Robber')
ax.plot(t, d_s, c='brown', label='Sheriff')

# Add lines where the robber is caught
plt.axvline(x=30, color='purple', linestyle='--')  # Vertical line at t=30
plt.axhline(y=75, color='purple', linestyle='--')  # Horizontal line at y=75

# Show the legend
plt.legend(['Robber', 'Sheriff', 'Catch Point'])

# Show the plot
plt.show()
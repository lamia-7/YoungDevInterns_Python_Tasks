
import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2π
x = np.linspace(0, 2 * np.pi, 100)

# Compute sine and cosine values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(8, 6))  # Set figure size

# Plot sine and cosine
plt.plot(x, y_sin, label='Sine', color='blue', linestyle='-', linewidth=2)
plt.plot(x, y_cos, label='Cosine', color='red', linestyle='--', linewidth=2)

# Add vertical lines for π/2, π, and 3π/2
plt.axvline(x=np.pi/2, color='green', linestyle=':', label='90°')
plt.axvline(x=np.pi, color='orange', linestyle=':', label='180°')
plt.axvline(x=3*np.pi/2, color='purple', linestyle=':', label='270°')

# Add titles and labels
plt.title('Sine and Cosine Graphs', fontsize=16)
plt.xlabel('Angle (degrees)', fontsize=12)
plt.ylabel('Value', fontsize=12)

# Add grid, legend, and axis ticks
plt.grid(alpha=0.5)
plt.legend(fontsize=12)
plt.xticks(
    [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
    ['0', '90°', '180°', '270°', '360°']
)
plt.ylim(-1.5, 1.5)  # Set y-axis range

# Add annotation
plt.annotate('Max Sine', xy=(np.pi/2, 1), xytext=(np.pi/2 + 0.5, 1.2),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# Show the plot
plt.show()


# In[ ]:





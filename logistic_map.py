import matplotlib.pyplot as plt
import numpy as np

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Parameters
r = 3.5  # Parameter r
num_iterations = 10  # Number of iterations
x_values = np.zeros(num_iterations)  # Initialize array for x values

# Initial condition
x_values[0] = 0.2

# Iterate function
for i in range(1, num_iterations):
    x_values[i] = logistic_map(r, x_values[i - 1])

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_values, marker='o')
plt.title(r'\textbf{Logistic map for} $r=3.5$')
plt.xlabel('Iterations $i$')
plt.ylabel('$x(i)$')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.minorticks_on()

# Save the figure
plt.savefig('logistic_map_r35.png', dpi=600)
plt.savefig('logistic_map_r35.pdf', format='pdf', bbox_inches='tight')

# Display the plot
plt.show()


import numpy as np

# Define the parameters for the Chebyshev and logistic maps
chebyshev_a = 2.8 # The parameter a for the Chebyshev map
logistic_r = 3.9 # The parameter r for the logistic map
initial_x = 0.5 # The initial value for x
initial_y = 0.3 # The initial value for y
num_iter = 1000 # The number of iterations to generate

# Define the Chebyshev map function
def chebyshev_map(x, a):
  return np.cos(a * np.arccos(x))

# Define the logistic map function
def logistic_map(x, r):
  return r * x * (1 - x)

# Initialize the arrays to store the generated values
x_values = np.zeros(num_iter)
y_values = np.zeros(num_iter)

# Set the initial values
x_values[0] = initial_x
y_values[0] = initial_y

# Generate the values using the coupled maps
for i in range(1, num_iter):
  # Update x using the Chebyshev map
  x_values[i] = chebyshev_map(x_values[i-1], chebyshev_a)
  # Update y using the logistic map
  y_values[i] = logistic_map(y_values[i-1], logistic_r)
  
  
print(x_values);

# Plot the generated values as a scatter plot
import matplotlib.pyplot as plt
plt.scatter(x_values, y_values, s=1, c='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Chaotic map generator using Chebyshev and logistic maps')
plt.show()



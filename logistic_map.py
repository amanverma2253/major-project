import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

def generate_bifurcation_plot(r_values, x0, num_iterations, num_points):
    bifurcation_plot = []

    for r in r_values:
        x = x0
        for _ in range(num_iterations):
            x = logistic_map(r, x)

        for _ in range(num_points):
            x = logistic_map(r, x)
            bifurcation_plot.append((r, x))

    return bifurcation_plot

def plot_bifurcation(bifurcation_plot):
    r_values, x_values = zip(*bifurcation_plot)
    plt.scatter(r_values, x_values, s=1, edgecolors='none')
    plt.xlabel('r (Parameter)')
    plt.ylabel('x (Population)')
    plt.title('Logistic Map Bifurcation Plot')
    plt.show()

# Parameters
r_values = [i/1000.0 for i in range(2000, 4001)]  # Adjust the range based on your preference
x0 = 0.5  # Initial value of x
num_iterations = 1000  # Number of iterations to reach equilibrium
num_points = 100  # Number of points to plot for each r

# Generate and plot bifurcation
bifurcation_data = generate_bifurcation_plot(r_values, x0, num_iterations, num_points)
plot_bifurcation(bifurcation_data)

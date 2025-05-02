import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def visualize_primes(limit):
    # Generate prime numbers
    primes = []
    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(np.sqrt(num)) + 1)):
            primes.append(num)

    # Create a grid
    size = int(np.ceil(np.sqrt(limit)))
    grid = np.zeros((size, size))

    # Fill the grid with prime numbers
    for n in primes:
        x = (n - 1) % size
        y = (n - 1) // size
        if y < size:
            grid[y, x] = n  # Store the prime number itself

    # Define the colors list
    colors = ["#FFFFFF", "#FFD700", "#FFA500", "#FF4500", "#FF0000"]

    # Create a custom colormap
    n_bins = len(colors)
    cmap = LinearSegmentedColormap.from_list("custom", colors, N=n_bins)

    # Plot the grid
    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap=cmap)
    plt.colorbar(label="Prime Numbers")
    plt.title(f"Visualization of Prime Numbers up to {limit}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


if __name__ == "__main__":
    limit = 100  # This will visualize primes up to 100
    visualize_primes(limit)

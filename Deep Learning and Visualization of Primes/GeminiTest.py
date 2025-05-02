print("Hello World")
for i in range(10):
    print(i)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# function to genrate a list of 20 random numbers
def generate_random_numbers():
    return np.random.rand(20)


# function to plot the random numbers
def plot_random_numbers(random_numbers):
    plt.plot(random_numbers)
    plt.show()


generate_random_numbers()
plot_random_numbers(generate_random_numbers())

#create a list of 20 random numbers between 20 and 25.
random_numbers = np.random.randint(20, 26, 20)
print(random_numbers)

#plot the random numbers
plt.plot(random_numbers)

#create a 3-d surface plot of a function
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with some transparency

# Plot contours on the surface
contours = ax.contour(X, Y, Z, zdir='z', offset=Z.min(), cmap='viridis', levels=10)

# Add a color bar for the contours
fig.colorbar(contours, ax=ax, shrink=0.5, aspect=5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()


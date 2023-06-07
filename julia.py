import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def julia(z, c, max_iter):
    for i in range(max_iter):
        if abs(z) > 2.0:
            return i
        z = z * z + c
    return max_iter

def generate_julia(width, height, x_min, x_max, y_min, y_max, max_iter, c):
    image = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            real = x_min + (x / width) * (x_max - x_min)
            imag = y_min + (y / height) * (y_max - y_min)
            z = complex(real, imag)
            iteration = julia(z, c, max_iter)
            image[x, y] = iteration
    return image


# Parameters for generating the Julia set
width = 800
height = 800

x_min, x_max = -0.5, 0.5
y_min, y_max = -0.5, 0.5

max_iter = 100

# Complex constant for the Julia set
c = complex(-.7, .270280)


# Generate the initial Julia set
image = generate_julia(width, height, x_min, x_max, y_min, y_max, max_iter, c)

# Plot the initial Julia set
fig, ax = plt.subplots()
plot = ax.imshow(image.T, cmap='hot', extent=(x_min, x_max, y_min, y_max))
plt.xlabel('Re')
plt.ylabel('Im')
plt.title('Julia Set')

# Create the animation

# Show the animation
plt.show()

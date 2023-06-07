import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for i in range(max_iter):
        if abs(z) > 2.0:
            return i
        z = z * z + c
    return max_iter

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    image = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            real = x_min + (x / width) * (x_max - x_min)
            imag = y_min + (y / height) * (y_max - y_min)
            c = complex(real, imag)
            iteration = mandelbrot(c, max_iter)
            image[x, y] = iteration
    return image

def plot_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    image = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

    plt.imshow(image.T, cmap='hot', extent=(x_min, x_max, y_min, y_max))
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.title('Mandelbrot Set')
    plt.show()

# Initial parameters
width = 800
height = 800

x_min, x_max = -2.5, 1.5
y_min, y_max = -2.0, 2.0

max_iter = 100

plot_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

# Interactive zoom and pan
while True:
    print("Enter 'q' to quit.")
    choice = input("Enter 'z' to zoom or 'p' to pan: ")

    if choice == 'q':
        break
    elif choice == 'z':
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2

        zoom_factor = float(input("Enter zoom factor: "))
        zoom_width = (x_max - x_min) / zoom_factor
        zoom_height = (y_max - y_min) / zoom_factor

        x_min = x_center - zoom_width / 2
        x_max = x_center + zoom_width / 2
        y_min = y_center - zoom_height / 2
        y_max = y_center + zoom_height / 2

        plot_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
    elif choice == 'p':
        x_offset = float(input("Enter horizontal offset: "))
        y_offset = float(input("Enter vertical offset: "))

        x_min += x_offset
        x_max += x_offset
        y_min += y_offset
        y_max += y_offset

        plot_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
    else:
        print("Invalid choice. Please try again.")

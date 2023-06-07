import numpy as np
import pygame
import sys

# Set the size of the grid
grid_size = (150, 100)
cell_size = 5
window_size = (grid_size[0] * cell_size, grid_size[1] * cell_size)

# Create the initial grid with two branches on either side
grid = np.zeros(grid_size, dtype=int)
grid[90:75, 95:50] = 1  # Left branch
grid[60:75, 50:55] = 1  # Right branch

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Conway's Game of Life")

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Create a new grid to store the next generation
    new_grid = np.zeros(grid_size, dtype=int)

    # Update each cell in the grid
    for i in range(1, grid_size[0] - 2):
        for j in range(1, grid_size[1] - 1):
            neighbor_count = (
                grid[i-1, j-1] + grid[i-1, j] + grid[i-1, j+1] +
                grid[i, j-1] + grid[i, j+1] +
                grid[i+1, j-1] + grid[i+1, j] + grid[i+1, j+1]
            )

            if grid[i, j] == 1:
                # Cell is alive
                if neighbor_count in [2, 3]:
                    new_grid[i, j] = 1
            else:
                # Cell is dead
                if neighbor_count == 1:
                    new_grid[i, j] = 1

    # Update the grid with the new generation
    grid = new_grid.copy()

    # Clear the window
    window.fill((255, 255, 255))

    # Draw the cells
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if grid[i, j] == 1:
                pygame.draw.rect(window, (0, 0, 0), (i * cell_size, j * cell_size, cell_size, cell_size))

    # Update the display
    pygame.display.update()
    clock.tick(10)  # Adjust the speed of the animation by changing the frames per second


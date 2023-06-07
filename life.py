import random
import pygame
import sys

# Pygame initialization
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Define the environment
available_resources = 100

# Define the organism
class Organism:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = random.randint(1, 4)

    def move(self):
        self.x += random.randint(-self.speed, self.speed)
        self.y += random.randint(-self.speed, self.speed)

        # Wrap around the screen
        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = HEIGHT
        elif self.y > HEIGHT:
            self.y = 0

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.size)

# Initialize the population
population_size = 400
population = [Organism(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(5, 20)) for _ in range(population_size)]

# Simulation settings
num_generations = 10000
generation_duration = 500  # in milliseconds

# Main simulation loop
for generation in range(num_generations):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Move and draw organisms
    for organism in population:
        organism.move()
        organism.draw()

    # Update the display
    pygame.display.flip()

    # Wait for the specified generation duration
    pygame.time.wait(generation_duration)

# End the simulation
pygame.quit()
sys.exit()

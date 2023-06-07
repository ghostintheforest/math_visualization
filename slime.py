import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particle Pattern Formation")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Define particle properties
num_particles = 100
particle_radius = 3
particle_color = GREEN

# Create the particles
particles = []
for _ in range(num_particles):
    particle = {
        'x': random.randint(particle_radius, width - particle_radius),
        'y': random.randint(particle_radius, height - particle_radius),
        'vx': random.uniform(-1, 1),
        'vy': random.uniform(-1, 1)
    }
    particles.append(particle)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Limit frame rate to 60 FPS
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update particle positions
    for particle in particles:
        particle['x'] += particle['vx']
        particle['y'] += particle['vy']
        
        # Boundary checking
        if particle['x'] < particle_radius or particle['x'] > width - particle_radius:
            particle['vx'] *= -1
        if particle['y'] < particle_radius or particle['y'] > height - particle_radius:
            particle['vy'] *= -1
    
    # Drawing
    screen.fill(BLACK)
    for particle in particles:
        pygame.draw.circle(screen, particle_color, (int(particle['x']), int(particle['y'])), particle_radius)
    
    pygame.display.flip()

# Quit the game
pygame.quit()

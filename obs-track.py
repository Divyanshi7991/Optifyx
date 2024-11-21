import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up simulation constants
WIDTH, HEIGHT = 800, 600
VEHICLE_SIZE = 50
OBSTACLE_SIZE = 100

# Set up vehicle and obstacle positions
vehicle_pos = np.array([WIDTH / 2, HEIGHT / 2])
obstacle_pos = np.array([WIDTH / 4, HEIGHT / 4])

# Set up vehicle velocity and acceleration
vehicle_vel = np.array([0, 0])
vehicle_acc = np.array([0, 0])

# Set up simulation loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update vehicle position and velocity
    vehicle_vel += vehicle_acc
    vehicle_pos += vehicle_vel

    # Check for collisions with obstacles
    if np.linalg.norm(vehicle_pos - obstacle_pos) < (VEHICLE_SIZE + OBSTACLE_SIZE) / 2:
        # Avoid obstacle
        vehicle_acc = np.array([-1, 0])

    # Draw simulation
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.draw.rect(screen, (0, 255, 0), (vehicle_pos[0], vehicle_pos[1], VEHICLE_SIZE, VEHICLE_SIZE))
    pygame.draw.rect(screen, (255, 0, 0), (obstacle_pos[0], obstacle_pos[1], OBSTACLE_SIZE, OBSTACLE_SIZE))
    pygame.display.flip()

    # Cap framerate
    pygame.time.delay(1000 // 60)

# Quit Pygame
pygame.quit()
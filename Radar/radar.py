import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radar Simulation")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FADED_GREEN = (0, 100, 0)

# Radar settings
center = (WIDTH // 2, HEIGHT // 2)
radius = 200
angle = 0  # Initial angle

# List of objects (random positions)
objects = []
blips = []  # Stores detected blips temporarily

clock = pygame.time.Clock()

# Generate random objects at different positions
for _ in range(10):  # Adjust the number of objects
    obj_angle = random.randint(0, 360)
    obj_distance = random.randint(50, radius)
    obj_x = center[0] + int(obj_distance * math.cos(math.radians(obj_angle)))
    obj_y = center[1] + int(obj_distance * math.sin(math.radians(obj_angle)))
    objects.append({"x": obj_x, "y": obj_y, "angle": obj_angle})

running = True
while running:
    screen.fill(BLACK)

    # Draw radar circle
    pygame.draw.circle(screen, GREEN, center, radius, 2)

    # Draw sweeping line
    end_x = center[0] + int(radius * math.cos(math.radians(angle)))
    end_y = center[1] + int(radius * math.sin(math.radians(angle)))
    pygame.draw.line(screen, GREEN, center, (end_x, end_y), 2)

    # Detect objects when the sweep reaches them
    for obj in objects:
        if abs(angle - obj["angle"]) < 2:  # If radar is near object
            blips.append({"x": obj["x"], "y": obj["y"], "life": 50})  # Add blip

    # Draw blips (fade effect)
    for blip in blips:
        pygame.draw.circle(screen, GREEN if blip["life"] > 30 else FADED_GREEN, (blip["x"], blip["y"]), 4)
        blip["life"] -= 1  # Reduce life span

    # Remove old blips
    blips = [b for b in blips if b["life"] > 0]

    # Update the angle
    angle = (angle + 2) % 360  # Sweep speed

    # Refresh display
    pygame.display.flip()
    clock.tick(30)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
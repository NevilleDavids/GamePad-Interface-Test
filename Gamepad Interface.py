import pygame
import sys
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_SIZE = 20
SPEED = 7  # Movement speed multiplier
ramval1 = 1
ramval2 = 1
ramval3 = 1


# Initialize Pygame and joystick
pygame.init()
pygame.joystick.init()

# Setup window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gamepad Square Mover")

# Check for gamepad
if pygame.joystick.get_count() == 0:
    print("No gamepad connected.")
    sys.exit()

# Use the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Gamepad connected: {joystick.get_name()}")

# Square starting position
x = SCREEN_WIDTH // 2 - SQUARE_SIZE // 2
y = SCREEN_HEIGHT // 2 - SQUARE_SIZE // 2

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.JOYBUTTONDOWN:
            ramval1 = random.randrange(0, 255, 3)
            ramval2 = random.randrange(0, 255, 3)
            ramval3 = random.randrange(0, 255, 3)

    # Read axis values (typically left analog stick: axis 0 = x, axis 1 = y)
    axis_x = joystick.get_axis(0)  # Horizontal
    axis_y = joystick.get_axis(1)  # Vertical

    # Apply deadzone to avoid drift
    deadzone = 0.1
    if abs(axis_x) < deadzone:
        axis_x = 0
    if abs(axis_y) < deadzone:
        axis_y = 0

    # Update square position
    x += int(axis_x * SPEED)
    y += int(axis_y * SPEED)

    # Clamp to screen
    x = max(0, min(SCREEN_WIDTH - SQUARE_SIZE, x))
    y = max(0, min(SCREEN_HEIGHT - SQUARE_SIZE, y))

    # Draw
    screen.fill((30, 30, 30))  # Dark background
    pygame.draw.rect(screen, (ramval1, ramval2, ramval3), (x, y, SQUARE_SIZE, SQUARE_SIZE))  # Cyan square
    pygame.display.flip()

    clock.tick(60)  # Limit to 60 FPS
    
print(ramval)
pygame.quit()

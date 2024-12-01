import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Image Display with Pygame")

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Load the image
image = pygame.image.load('steve buscemi.JPG')

# Get the rect of the image
image_rect = image.get_rect()

# Initial position of the image
image_rect.center = (width // 2, height // 2)

# Speed of the image movement
speed_x, speed_y = 5, 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the image
    image_rect.x += speed_x
    image_rect.y += speed_y

    # Bounce the image off the edges
    if image_rect.left < 0 or image_rect.right > width:
        speed_x = -speed_x
    if image_rect.top < 0 or image_rect.bottom > height:
        speed_y = -speed_y

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the image
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()
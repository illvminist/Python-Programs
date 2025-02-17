from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *  # This includes MOUSEMOTION and other necessary constants
import numpy as np

# Planet Class to manage each planet
class Planet:
    def __init__(self, size, distance, color, speed):
        self.size = size
        self.distance = distance
        self.color = color
        self.speed = speed
        self.angle = 0

    def draw(self):
        glPushMatrix()
        glRotatef(self.angle, 0, 1, 0)  # Rotate planet around Earth
        glTranslatef(self.distance, 0, 0)  # Move the planet along its orbit

        # Draw the planet as a sphere using GLU
        glColor3fv(self.color)
        self.draw_sphere(self.size)

        glPopMatrix()

    def draw_sphere(self, radius):
        # Create a new quadric object for the sphere
        quadric = gluNewQuadric()
        gluSphere(quadric, radius, 20, 20)  # Draw sphere with a given radius

    def update(self):
        self.angle += self.speed
        if self.angle >= 360:
            self.angle = 0

# Set up OpenGL
def setup_opengl():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0, 0, 0, 1)
    gluPerspective(45, 1, 0.1, 100.0)
    glTranslatef(0.0, 0.0, -20)

# Draw Earth at the center
def draw_earth():
    glColor3fv((0, 0, 1))  # Earth is blue
    glutSolidSphere(2, 20, 20)  # Earth is a sphere with radius 2

# Initialize planets
def initialize_planets():
    # Planets with size, distance from Earth, color, and orbital speed
    planets = [
        Planet(0.4, 4, (1, 0, 0), 0.3),  # Mercury (Red)
        Planet(0.8, 6, (0, 1, 0), 0.2),  # Venus (Green)
        Planet(1, 8, (0, 0, 1), 0.15),   # Earth (Blue)
        Planet(0.6, 10, (1, 1, 0), 0.1),  # Mars (Yellow)
        Planet(1.5, 14, (1, 0, 1), 0.08), # Jupiter (Purple)
        Planet(1.2, 18, (0, 1, 1), 0.05), # Saturn (Cyan)
        Planet(0.9, 22, (1, 0.5, 0), 0.04), # Uranus (Orange)
        Planet(0.8, 26, (0.5, 0, 0.5), 0.02) # Neptune (Dark Purple)
    ]
    return planets

# Main function to run the simulation
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    setup_opengl()

    planets = initialize_planets()

    # Main loop
    clock = pygame.time.Clock()
    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw Earth at the center
        draw_earth()

        # Draw each planet and update their positions
        for planet in planets:
            planet.update()
            planet.draw()

        pygame.display.flip()
        clock.tick(60)

        # Handle user input (exit and interaction)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    x, y = event.pos
                    glRotatef(x / 2, 1, 0, 0)  # Rotate based on mouse movement
                    glRotatef(y / 2, 0, 1, 0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up (Zoom in)
                    glTranslatef(0, 0, 1)
                if event.button == 5:  # Scroll down (Zoom out)
                    glTranslatef(0, 0, -1)

if __name__ == "__main__":
    main()

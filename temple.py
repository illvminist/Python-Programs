import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time

# Initialize prophecy text
prophecies = [
    "In the last days, the mountain of the Lord's temple will be established. (Isaiah 2:2)",
    "The glory of this latter temple shall be greater than the former. (Haggai 2:9)",
    "Behold, the dwelling place of God is with man. (Revelation 21:3)"
]

# Helper to draw text
def draw_text(text, position, font_size=32, color=(1, 1, 1)):
    font = pygame.font.SysFont('Arial', font_size, bold=True)
    text_surface = font.render(text, True, [int(c * 255) for c in color])
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    width, height = text_surface.get_size()
    glRasterPos3f(position[0], position[1], position[2])
    glDrawPixels(width, height, GL_RGBA, GL_UNSIGNED_BYTE, text_data)

# Temple base
def draw_base():
    glColor3f(0.8, 0.7, 0.5)
    glBegin(GL_QUADS)
    for x, z in [(-5, -5), (5, -5), (5, 5), (-5, 5)]:
        glVertex3f(x, 0, z)
    glEnd()

# Holy Place
def draw_holy_place():
    glColor3f(1, 0.84, 0)  # Golden walls
    glBegin(GL_QUADS)
    for x, y, z in [(-2, 0, -2), (2, 0, -2), (2, 4, -2), (-2, 4, -2)]:
        glVertex3f(x, y, z)
    glEnd()

# Scrolling text
def scroll_text(y_offset):
    glPushMatrix()
    glTranslatef(-4, y_offset, -8)
    for idx, line in enumerate(prophecies):
        draw_text(line, (0, idx * -0.5, 0))
    glPopMatrix()

# Main display
def main():
    pygame.init()
    display = (1000, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0.0, -5, -20)
    
    y_offset = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        y_offset += 0.02  # Adjust for text scrolling speed

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_base()
        draw_holy_place()
        scroll_text(y_offset)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

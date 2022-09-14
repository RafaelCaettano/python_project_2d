import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertice = (
    (-3, 0),
    (0, 2),
    (3, 0),
    (0, -4)
)

aresta = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0)
)


def square():
    glBegin(GL_LINES)

    for temp_aresta in aresta:
        for vertex in temp_aresta:
            glVertex2iv(vertice[vertex])
    glEnd()


def main():
    pygame.init()
    display = (700, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(80, (display[0] / display[1]), 1, 20)

    glTranslatef(0, 0, -5)
    glRotatef(45, 0, 0, 0)
    glColor3f(1, 1, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        square()
        pygame.display.flip()


main()

import glfw
from OpenGL.GL import *

glfw.init()
window = glfw.create_window(800, 600, "Flag of Surinam", None, None)
glfw.make_context_current(window)

while not glfw.window_should_close(window):
    #зелёный фон
    glClearColor(0, 1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)

    #белый фон
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUAD_STRIP)
    glVertex3f(-1, -0.6, 0.0)
    glVertex3f(1, -0.6, 0.0)
    glVertex3f(-1, 0.6, 0.0)
    glVertex3f(1, 0.6, 0.0)
    glEnd()

    #красный фон
    glColor3f(1, 0, 0)
    glBegin(GL_QUAD_STRIP)
    glVertex3f(-1, -0.45, 0.0)
    glVertex3f(1, -0.45, 0.0)
    glVertex3f(-1, 0.45, 0.0)
    glVertex3f(1, 0.45, 0.0)
    glEnd()

    #жёлтая звезда(остриём вниз)
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.3, 0.08, 0.0)
    glVertex3f(0.3, 0.08, 0.0)
    glVertex3f(0.0, -0.2, 0.0)
    glEnd()

    # жёлтая звезда(острём вправо)
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.2, -0.39, 0.0)
    glVertex3f(0.11, -0.1, 0.0)
    glVertex3f(0.0, 0.4, 0.0)
    glEnd()

    # жёлтая звезда(острём влево)
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.05, -0.15, 0.0)
    glVertex3f(0.21, -0.4, 0.0)
    glVertex3f(0.0, 0.4, 0.0)
    glEnd()


    glfw.swap_buffers(window)
    glfw.poll_events()
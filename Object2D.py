from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys

window_width = 800
window_height = 600

# Global variabel
objects = []
current_color = (1.0, 1.0, 1.0)
line_width = 2
start_point = None
mode = 'line'  # 'point', 'line', 'rect', 'ellipse'

# Drawing Object Function

def draw_point(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_line(p1, p2):
    glLineWidth(line_width)
    glBegin(GL_LINES)
    glVertex2f(*p1)
    glVertex2f(*p2)
    glEnd()

def draw_rect(p1, p2):
    glLineWidth(line_width)
    glBegin(GL_LINE_LOOP)
    glVertex2f(p1[0], p1[1])
    glVertex2f(p2[0], p1[1])
    glVertex2f(p2[0], p2[1])
    glVertex2f(p1[0], p2[1])
    glEnd()

def draw_ellipse(p1, p2):
    glLineWidth(line_width)
    glBegin(GL_LINE_LOOP)
    cx = (p1[0] + p2[0]) / 2
    cy = (p1[1] + p2[1]) / 2
    rx = abs(p1[0] - p2[0]) / 2
    ry = abs(p1[1] - p2[1]) / 2
    for i in range(360):
        angle = i * 3.14159 / 180
        x = cx + rx * cos(angle)
        y = cy + ry * sin(angle)
        glVertex2f(x, y)
    glEnd()

# Coordinate Convert Function

def screen_to_gl(x, y):
    return (x / window_width * 2 - 1, -(y / window_height * 2 - 1))

# Mouse function

def mouse_func(button, state, x, y):
    global start_point
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        gl_x, gl_y = screen_to_gl(x, y)
        start_point = (gl_x, gl_y)
    elif button == GLUT_LEFT_BUTTON and state == GLUT_UP and start_point:
        gl_x, gl_y = screen_to_gl(x, y)
        end_point = (gl_x, gl_y)
        objects.append((mode, start_point, end_point, current_color))
        start_point = None
        glutPostRedisplay()

# Keyboard Function

def keyboard_func(key, x, y):
    global current_color, line_width, mode
    if key == b'r':
        current_color = (1.0, 0.0, 0.0)
    elif key == b'g':
        current_color = (0.0, 1.0, 0.0)
    elif key == b'b':
        current_color = (0.0, 0.0, 1.0)
    elif key == b'+':
        line_width += 1
    elif key == b'-':
        line_width = max(1, line_width - 1)
    elif key == b'1':
        mode = 'point'
    elif key == b'2':
        mode = 'line'
    elif key == b'3':
        mode = 'rect'
    elif key == b'4':
        mode = 'ellipse'
    glutPostRedisplay()

# Display Function

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    for obj in objects:
        shape, p1, p2, color = obj
        glColor3f(*color)
        if shape == 'point':
            draw_point(*p1)
        elif shape == 'line':
            draw_line(p1, p2)
        elif shape == 'rect':
            draw_rect(p1, p2)
        elif shape == 'ellipse':
            draw_ellipse(p1, p2)
    glFlush()

# Pre-SetUp

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

# Main

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Modul A: Objek 2D - PyOpenGL")
init()
glutDisplayFunc(display)
glutMouseFunc(mouse_func)
glutKeyboardFunc(keyboard_func)
glutMainLoop()

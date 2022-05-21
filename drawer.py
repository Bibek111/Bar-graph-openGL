import OpenGL
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from scipy import rand
WINDOW_SIZE = 2000

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-0.025, 1.0,-0.025,1.0)

def draw(config):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 1)
    glPointSize(5.0)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    plot_polygons(config)    
    glFlush()

def plot_polygons(config):    
    datas = config.get("datas")
    N = len(datas)
    max_data = max(datas)
    datas = [(data/max_data)*WINDOW_SIZE*0.9 for data in datas]
    for i in range (N):
        X = WINDOW_SIZE/N
        n= random.random()
        glColor3f(rand()%255, rand()%255, rand()%255)
        bar = [(X*i,0),(X*(i+1),0),(X*(i+1),datas[i]),(X*i,datas[i])]
        draw_polygon(bar)
    lines = config.get("lines")
    glColor3f(1,0,0)
    draw_lines(lines)

def draw_lines(lines):
    for line in lines:
        if line == None:
            continue
        x1,y1 = line[0]
        x2,y2 = line[1]
        glBegin(GL_LINES)
        glVertex2f(x1/WINDOW_SIZE, y1/WINDOW_SIZE)
        glVertex2f(x2/WINDOW_SIZE, y2/WINDOW_SIZE)
        glEnd()
    
def draw_polygon(vertexes):
    glBegin(GL_POLYGON)
    for v in vertexes:
        glVertex2f(v[0]/WINDOW_SIZE, v[1]/WINDOW_SIZE)
    glEnd()

def drawer(config):
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("BarGraph")
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    init()
    glutDisplayFunc(lambda:draw(config))
    glutMainLoop()



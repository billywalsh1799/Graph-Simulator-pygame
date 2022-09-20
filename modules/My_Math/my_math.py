from math import *
import pygame
from modules.assets.colors import *

def distance(p1,p2):
    d=(p1[0]-p2[0])**2+(p1[1]-p2[1])**2
    return sqrt(d)

#add line intersectoin and rotation methods

#wrongone
def line_circle_wrong(e,v):
    #first determine line equation
    x1,y1=e.extents[0].pos
    x2,y2=e.extents[1].pos
    #slope
    a=(y1-y2)/(x1-x2)
    #intercept
    b=y1-a*x1
    #circle elements
    xc,yc=v.pos
    R=v.radius
    #quadratic formula coefficients
    A=1+a**2
    B=-2*xc+2*a*b-2*a*yc
    C=(xc**2)+(yc**2)+(b**2)-2*b*yc-(R**2)
    #solutions
    delta=(B**2)-4*A*C
    X1=(-B-sqrt(delta))/(2*A)
    X2=(-B+sqrt(delta))/(2*A)
    #result
    if distance(a*X1+b,e.extents[0].pos)<distance(a*X2+b,e.extents[0].pos):
        return X1,a*X1+b
    else:
        return X2,a*X2+b

def line_circle(c,l,index):
    #exception horizantl and vertical line
    #if l[0][0]==l[1][0] or l[0][1]==l[1][1]

    #first determine line equation
    x1,y1=l[0]
    x2,y2=l[1]
    
    if x1==x2:
        xc,yc=c[0]
        R=c[1]
        p1=xc,yc-R
        p2=xc,yc+R
        p3=l[index]
        if distance(p1,p3)<distance(p2,p3):
            return p1
        else:
            return p2
    
    elif y1==y2:
        xc,yc=c[0]
        R=c[1]
        p1=xc+R,yc
        p2=xc-R,yc
        p3=l[index]
        if distance(p1,p3)<distance(p2,p3):
            return p1
        else:
            return p2
    else:
        
        #slope
        a=(y1-y2)/(x1-x2)
        #intercept
        b=y1-a*x1
        #circle elements
        xc,yc=c[0]
        R=c[1]
        #quadratic formula coefficients
        A=1+a**2
        B=-2*xc+2*a*b-2*a*yc
        C=(xc**2)+(yc**2)+(b**2)-2*b*yc-(R**2)
        #solutions
        delta=(B**2)-4*A*C
        X1=(-B-sqrt(delta))/(2*A)
        X2=(-B+sqrt(delta))/(2*A)
        #result
        #return (X1,a*X1+b),(X2,a*X2+b)
        p1=X1,a*X1+b
        p2=X2,a*X2+b
        p3=l[index]

        if distance(p1,p3)<distance(p2,p3):
            return p1
        else:
            return p2


def rotation(c,x,t):
    # c center of rotation t angle x point to rotate
    l=[0,0]
    l[0]=cos(t)*(x[0]-c[0])-sin(t)*(x[1]-c[1])+c[0]
    l[1]=sin(t)*(x[0]-c[0])+cos(t)*(x[1]-c[1])+c[1]
    return l

def draw_arrow(c,l,index,win,color):
    #edge intersection with vertex
    inter1=line_circle(c,l,index)
    c2=(inter1,15)

    #translate the point 
    inter2=line_circle(c2,l,index)

    #rotate the point
    rot1=rotation(inter1,inter2,pi/4)
    rot2=rotation(inter1,inter2,-pi/4)

    #drawing the arrow
    pygame.draw.polygon(win,color,(rot1,rot2,inter1))
    

    

    
    
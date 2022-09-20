import pygame
from modules.assets.colors import *
from modules.My_Math.my_math import *


class edge:
    def __init__(self,pos,extents,directed,w=1): 
        self.position=pos
        self.extents=extents
        self.weight=w
        self.color=black
        self.directed=directed
        
    def make(self,c):
        self.color=c
    def draw_edge(self,win):
        pygame.draw.line(win,self.color,self.position[0],self.position[1],5)
        if self.directed:
            c=self.extents[1].position,30
            l=self.position
            draw_arrow(c,l,0,win,self.color)
    def __str__(self):
        return str(self.extents[0])+"-"+str(self.extents[1])
    
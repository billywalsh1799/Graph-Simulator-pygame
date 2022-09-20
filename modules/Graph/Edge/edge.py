import pygame
from modules.assets.colors import *
from modules.My_Math.my_math import *


class edge:
    def __init__(self,pos,extents,w=1): 
        self.position=pos
        self.extents=extents
        self.weight=w
        self.color=black
    def make(self,c):
        self.color=c
    def draw_edge(self,win,directed=False):
        pygame.draw.line(win,self.color,self.position[0],self.position[1],5)
        if directed:
            c=self.extents[1].position,30
            l=self.position
            draw_arrow(c,l,0,win)
    def __str__(self):
        return str(self.extents[0])+"-"+str(self.extents[1])
    
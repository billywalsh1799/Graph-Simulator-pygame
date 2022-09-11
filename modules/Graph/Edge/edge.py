import pygame
from modules.assets.colors import *


class edge:
    def __init__(self,pos,extents,w=1): 
        self.position=pos
        self.extents=extents
        self.weight=w
        self.color=black
    def make_white(self):
        self.color=white
    def make_black(self):
        self.color=black
    def make_Periwinkle(self):
        self.color=Periwinkle
    
    def draw_edge(self,win):
        pygame.draw.line(win,self.color,self.position[0],self.position[1],5)
    def __str__(self):
        return str(self.extents[0])+"-"+str(self.extents[1])
import pygame
from modules.assets.colors import *




def draw_text(txt,pos,color,win):
    font_obj=pygame.font.SysFont('consolas', 20)
    text_surface_obj = font_obj.render(txt,True,color)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center =pos
    win.blit(text_surface_obj, text_rect_obj)


class vertex:
    def __init__(self,pos,id):
        self.id=id
        self.position=pos
        self.color=turquoise
        self.neighbors=set()
        self.radius=30
        self.deg=0
    def make_blue(self):
        self.color=light_red
    def make_turqoise(self):
        self.color=turquoise
    def make_green(self):
        self.color=green
        
    def make_purple(self):
        self.color=purple
    def make_Periwinkle(self):
        self.color=Periwinkle
    
    def draw_vertex(self,win):
        pygame.draw.circle(win,self.color,self.position,self.radius,0)
        draw_text(str(self.id),self.position,black,win)
    def __str__(self):
        return str(self.id)
    def make(self,c):
        self.color=c
import time
import pygame
from modules.assets.colors import *


def draw_text(txt,pos,color,win):
    font_obj=pygame.font.SysFont('consolas', 20)
    text_surface_obj = font_obj.render(txt,True,color)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center =pos
    win.blit(text_surface_obj, text_rect_obj)

         
def delay(t):
    
    start=time.time()
    while 1:
        end=time.time()
        if end-start>t:
            break
        pygame.event.pump()


def temptext(stack,win):
    recta=pygame.Rect(0,855,1500,300)
    pygame.draw.rect(win,beige,recta)
    pygame.display.update()
    
    txt=''
    for x in stack : 
            txt=txt+'  '+str(x.id) 
    draw_text(txt,(750,890),black,win)
    pygame.display.update()
    delay(0.3)
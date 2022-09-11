import pygame
from modules.assets.colors import *



class w_button:
    button_col=black
    hover_col=gray
    click_col=light_red
    width=100
    height=70
    size_e=30
    size_w=25
    
    def __init__(self,x,y,text_e,text_w,win):
        self.x=x
        self.y=y
        self.text_e=text_e
        self.text_w=text_w
        self.win=win
        self.clicked=False
        self.pressed=False
        pos=x+(w_button.width/2)-8*len(text_w)
        self.border=pos+len(text_w)*14
        self.cur=pos+len(text_w)*14
    def draw_button(self):
        action=False
        pos=pygame.mouse.get_pos()
        button_rect=pygame.Rect(self.x,self.y,self.width,self.height)
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked=True            
                pygame.draw.rect(self.win,self.click_col,button_rect,3)
                pygame.draw.line(self.win,self.click_col,(self.x,self.y+self.height//2),(self.x+self.width-1,self.y+self.height//2),3)
                
            elif pygame.mouse.get_pressed()[0]==0 and self.clicked:
                self.clicked=False
                action=True
            else:
                pygame.draw.rect(self.win,self.hover_col,button_rect,3)
                pygame.draw.line(self.win,self.hover_col,(self.x,self.y+self.height//2),(self.x+self.width-1,self.y+self.height//2),3)
        
        else:
            pygame.draw.rect(self.win,self.button_col,button_rect,3)
            pygame.draw.line(self.win,black,(self.x,self.y+self.height//2),(self.x+self.width-1,self.y+self.height//2),3)
        
        
        font1=pygame.font.SysFont('consolas',self.size_e)
        font2=pygame.font.SysFont('consolas',self.size_w)
        
        
        
        edge= font1.render(self.text_e,True,black)
        edge_len = edge.get_width()
        positions =(self.x+(self.width//2)-(edge_len//2),self.y+5)
        self.win.blit(edge,positions)
        
        weight=font2.render(self.text_w,True,black)
        position=(self.x+(self.width/2)-8*len(self.text_w),self.y+(3/4)*self.height-12)
        self.win.blit(weight,position)
        if self.pressed:
            pygame.draw.line(self.win,black,(self.cur,position[1]),(self.cur,position[1]+23))
        
        return action
import pygame
from modules.assets.colors import *





class button():
    button_col=25,190,225
    click_col=50,150,255
    hover_col=75,225,255
   
    text_col=255,255,255
    width=180
    height=40
    font_size=20
    shading=1

    def __init__(self,x,y,text,win):
        self.x=x
        self.y=y
        self.text=text
        self.clicked=False
        self.win=win
    def draw_button(self):
        action=False
        temp=self.text_col
        pos=pygame.mouse.get_pos()
        button_rect=pygame.Rect(self.x,self.y,self.width,self.height)
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked=True            
                if self.shading:
                    pygame.draw.rect(self.win,self.click_col,button_rect)
                else:
                    self.text_col=gray
                    
                
            elif pygame.mouse.get_pressed()[0]==0 and self.clicked:
                self.clicked=False
                action=True
            else:
                if self.shading:
                    pygame.draw.rect(self.win,self.hover_col,button_rect)
                else:
                    
                    self.text_col=white
        
        else:
            pygame.draw.rect(self.win,self.button_col,button_rect)
        if self.shading:
            pygame.draw.line(self.win,white,(self.x,self.y),(self.x+self.width,self.y),2)
            pygame.draw.line(self.win,white,(self.x,self.y),(self.x,self.y+self.height),2)
            pygame.draw.line(self.win,black,(self.x,self.y+self.height),(self.x+self.width,self.y+self.height),2)
            pygame.draw.line(self.win,black,(self.x+self.width,self.y),(self.x+self.width,self.y+self.height),2)
        
        
        font_obj=pygame.font.SysFont('consolas',self.font_size)
        text_img = font_obj.render(self.text,True,self.text_col)
        text_len = text_img.get_width()
        positions =(self.x+(self.width//2)-(text_len//2),self.y+5)
        self.win.blit(text_img,positions)
        self.text_col=temp
        return action
    
    #new method only for directed button
    
    def set_text(self,txt):
        self.text=txt
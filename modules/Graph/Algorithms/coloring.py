import pygame
from modules.assets.colors import *
from modules.My_Methods.my_methods import delay




def coloredneigh(x,colored,num):
        for i in x.neighbors:
            if colored[i]==num : return True
        return False 

def COLORSS(V,E,win):
        BLACK = (0, 0, 0) ;RED = (255, 0, 0);YELLOW = (255, 255, 0) 
        GRAY = (127, 127, 127);GREEN = (0, 255, 0);CYAN = (0, 255, 255) 
        WHITE = (255, 255, 255);BLUE = (0, 0, 255);MAGENTA = (255, 0, 255)
 

        
        l=sorted(V , key=lambda x : x.deg ,reverse=True)
        colored={i:False for i in V}
        colors=[WHITE,RED,YELLOW,GREEN,CYAN,BLUE,BLACK,MAGENTA,GRAY]
        num=1
        
        for i in range(len(l)):
            if colored[l[i]]==False : 
                colored[l[i]]=num
                l[i].make(colors[num])
                l[i].draw_vertex(win)
                pygame.display.update()
                delay(0.6)
                
                for j in range(i+1,len(l)):
                    if colored[l[j]]==False and (not coloredneigh(l[j],colored,num))  : 
                        colored[l[j]]=num
                        l[j].make(colors[num])
                        l[j].draw_vertex(win)
                        pygame.display.update()
                        delay(0.5)
                num+=1
                delay(2)
        for i in V :
            i.make(turquoise)
import pygame
from modules.assets.colors import *
from modules.My_Methods.my_methods import *



        
def dfs(v1,V,E,win):
    visited={v1}
    unvisited={edge:0 for edge in E}
    self_visited={v:False for v in V}
    self_visited[v1]=True
    stack=[v1]
    def color_edges(E):
        for edge in E:
            if edge.extents[0].color==light_red and edge.extents[1].color==light_red and unvisited[edge]==0:
                edge.make(white)
                edge.draw_edge(win)
                edge.extents[0].draw_vertex(win)
                edge.extents[1].draw_vertex(win)
                unvisited[edge]=1
                delay(0.5)
                
                
    v1.make(green)
    v1.draw_vertex(win)
    pygame.display.update()
    
    delay(1)
    

    
    v1.make(light_red)
    v1.draw_vertex(win)
    pygame.display.update()
    
    temptext(stack,win)
    delay(0.5)
    
    
    
    
    
    for vertex in v1.neighbors:
        stack.append(vertex) 
        temptext(stack,win)
    
    
    while stack!=[]:
        
        x=stack.pop()
        delay(0.5)
        temptext(stack,win)
        
        visited.add(x)
        if self_visited[x]==False:
            x.make(green)
            x.draw_vertex(win)
            pygame.display.update()
            delay(0.5)
            
            
            
            


            x.make(light_red)
            x.draw_vertex(win)
            delay(0.5)
            
            
            color_edges(E)
            
            pygame.display.update()
            
            delay(0.5)
            
            
            
            
            for vertex in x.neighbors:
                stack.append(vertex)
                temptext(stack,win)
                delay(1)
                
            self_visited[x]=True
    
    temptext(stack,win) 
    
    delay(0.5)
    
    
    
    
    for vertex in V:
        vertex.make(turquoise)
        vertex.draw_vertex(win)
    for edge in E:
        edge.make(black)
        edge.draw_edge(win)
    
    pygame.display.update()
    pygame.event.pump()
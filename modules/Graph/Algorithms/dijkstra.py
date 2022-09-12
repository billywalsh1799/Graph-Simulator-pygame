import pygame
from modules.My_Methods.my_methods import delay
from modules.assets.colors import *

def mini(path):
    x=list(path.keys())[0]
    y=path[x][0]
    for v in path:
        if path[v][0]<y:
            y=path[v][0]
            x=v
    return x
            

              
def dijkstra(s,d,V,E,win):
        visited={i:0 for i in V}
        path={i:[float("inf"),""] for i in V}
        path[s]=[0,""]
        temp={s:[0,""]}
        
        while temp:
            key=mini(temp)
            used_edges=set()
            used_vertices=set()
            
            key.make(green)
            key.draw_vertex(win)
            pygame.display.update()
            delay(1)
            
            visited[key]=1
            for v in key.neighbors:
                
                if visited[v]:
                    continue
                
                for edge in E:
                    if edge.extents==(key,v) or edge.extents==(v,key):
                        tempo=edge
                        used_edges.add(edge)
                        used_vertices.add(v)
                        edge.make(white)
                        edge.draw_edge(win)
                        key.draw_vertex(win)
                        v.draw_vertex(win)
                        
                        pygame.display.update()
                        delay(1)
                        break
                x=path[v][0]
                y=path[key][0]+tempo.weight 
                if  y<x:
                    path[v]=[y,key]
                    temp[v]=[y,key]
            
            delay(1)
            
            for edge in used_edges:
                edge.make(black)
                edge.draw_edge(win)
            for vertex in used_vertices:
                vertex.make(turquoise)
                vertex.draw_vertex(win)
            key.make(light_red)
            key.draw_vertex(win) 
            pygame.display.update()
            if key==d:
                break
            del temp[key]
        chemin=[d]
        current=d
        while current!=s:
            current=path[current][1]
            chemin.append(current)
        used_edges=set()
        used_vertices=set()
        for i in range(len(chemin)-1,0,-1):
            
            for edge in E:
                if edge.extents==(chemin[i],chemin[i-1]) or edge.extents==(chemin[i-1],chemin[i]):
                    tempo=edge
                    used_edges.add(edge)
                    used_vertices.add(v)
                    edge.make(Periwinkle)
                    edge.draw_edge(win)
                    
                    chemin[i-1].make(Periwinkle)
                    chemin[i-1].draw_vertex(win)
                    
                    chemin[i].make(Periwinkle)
                    chemin[i].draw_vertex(win)
                    
                    
                    pygame.display.update()
                    delay(1)
                    break
        delay(2)
        for edge in E:
            edge.make(black)
            edge.draw_edge(win)
        
        for vertex in V:
            vertex.make(turquoise)
            vertex.draw_vertex(win)
        
        
        pygame.display.update()
        pygame.event.pump()
        
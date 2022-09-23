import pygame
from modules.Graph.Vertex.vertex  import vertex
from math import*
from modules.My_Math.my_math import distance






def adding_vertices(counter,V): 
    pos=pygame.mouse.get_pos()
    if pos[0]<1545 and pos[1]<820:
        v=vertex(pos,counter[0])
        V.add(v)
        counter[0]+=1
    
def removing_vertices(V,E,W,junk):
    pygame.event.pump()
    pos=pygame.mouse.get_pos()
    l=[]
    for vertex in V:
        if distance(vertex.position,pos)<=vertex.radius:
            pygame.event.pump()
            for e in E:
                if vertex in e.extents:
                    l.append(e)
            for i in l:
                junk.append(W[i].x)
                del W[i]
                E.remove(i)
            for j in vertex.neighbors:
                if vertex in j.neighbors:
                    j.neighbors.remove(vertex)
            V.remove(vertex)
            break
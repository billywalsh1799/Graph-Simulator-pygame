import pygame
from  modules.Graph.Edge.edge import edge
from modules.Buttons.w_button import w_button

def adding_edges(win,E,pos,v1,v2,W,junk,start,directed):
    v1.neighbors.add(v2)
    if not(directed):
        v2.neighbors.add(v1)
    v2.deg+=1
    v1.deg+=1
    e=edge(pos,(v1,v2),directed)
    E.add(e)
    if junk:
        x=junk.pop(0)
        tab=w_button(x,880,str(e),str(e.weight),win)
        W[e]=tab
    else:
        tab=w_button(start[0],880,str(e),str(e.weight),win)
        start[0]+=101
        W[e]=tab
    


def removing_edges(E,v1,v2,W,junk,directed):
    v1.neighbors.remove(v2)
    if not(directed):
        v2.neighbors.remove(v1)
    v2.deg-=1
    v1.deg-=1
    for e in E:
        if e.position==[v1.position,v2.position] or e.position==[v2.position,v1.position]:
            E.remove(e)
            junk.append(W[e].x)
            del W[e]
            break
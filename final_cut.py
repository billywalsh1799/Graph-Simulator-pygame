import pygame
from math import*
from modules.Buttons.button import button

from modules.Graph.Vertex.methods import adding_vertices,removing_vertices
from modules.Graph.Edge.methods import adding_edges,removing_edges

from modules.Graph.Algorithms.dfs import dfs
from modules.Graph.Algorithms.bfs import bfs
from modules.Graph.Algorithms.dijkstra import dijkstra
from modules.Graph.Algorithms.coloring import COLORSS
from modules.assets.colors import *

from modules.My_Methods.my_methods import delay
from modules.My_Math.my_math import *




pygame.init()
width,height=1800,980
win=pygame.display.set_mode((width,height))





         
s=0,0
e=500,500
fps=60
def main():
    
    start=[20,880]
    V=set()
    E=set()
    W={} 
    junk=[]
    
    beige=234,210,168
    e=0
    clock=pygame.time.Clock()
    run=True
    
    
    algo_pressed=False
    
    add_v=button(1600,100,"add vertex",win)
    rm_v=button(1600,200,"remove vertex",win)
    add_e=button(1600,300,"add edge",win)
    rm_e=button(1600,400,"remove edge",win)
    algo=button(1600,500,"Algorithms",win)

    directed=button(1600,20,"Directed",win)
    
    menu={add_v,rm_v,add_e,rm_e,algo}


    DFS=button(1660,600,"DFS",win)
    DFS.height=22
    DFS.width=45
    DFS.text_col=black
    DFS.button_col=beige
    DFS.shading=0

    BFS=button(1660,650,"BFS",win)
    BFS.height=22
    BFS.width=45
    BFS.button_col=beige
    BFS.text_col=black
    BFS.shading=0


    DIJKSTRA=button(1645,700,"DIJKSTRA",win)
    DIJKSTRA.height=22
    DIJKSTRA.width=85
    DIJKSTRA.button_col=beige
    DIJKSTRA.text_col=black
    DIJKSTRA.shading=0
    
    
    
    COLORS=button(1660,750,"COLORS",win)
    COLORS.height=22
    COLORS.width=45
    COLORS.button_col=beige
    COLORS.text_col=black
    COLORS.shading=0
    
    algo_choices={DFS,BFS,DIJKSTRA,COLORS}

    
    
    c=[0]
    pos=[(0,0),(0,0)]
    actions={add_v:0,rm_v:0,add_e:0,rm_e:0,algo:0}
    algos={DFS:0,BFS:0,DIJKSTRA:0,COLORS:0}
    arrow_left = 0
    
    

    
    
    
    
    w_action=False
    
    
    while run:
        clock.tick(fps)
        win.fill(beige)
        pygame.draw.line(win,black,(1575,0),(1575,850),3)
        pygame.draw.line(win,black,(0,850),(1575,850),3)

        #rotation test starts

        """ pygame.draw.line(win,black,(111,111),(555,555),3)

        pygame.draw.circle(win,turquoise,(555,555),30,0)

        pygame.draw.circle(win,turquoise,(111,111),30,0)

        c1=((555,555),30)
        c2=((111,111),30)
        l=((111,111),(555,555))
        index=0
        draw_arrow(c1,l,index,win)
        draw_arrow(c2,l,1,win) """

        
        #rotatoin test ends

        for but in menu: 
            if but.draw_button():
                for action in actions:
                    if action==but:
                        actions[but]=1
                    else:
                        actions[action]=0
                if but==algo:
                    algo_pressed=not(algo_pressed)
                else:
                    algo_pressed=False
                for e in W:
                    W[e].pressed=False
        

        #directed button test starts

        if directed.draw_button() and not(E):
            if directed.text=="Directed":
                directed.set_text("Undirected")
            else:
                directed.set_text("Directed")


        #directed button test ends
             
        if E:
            for edge in E:
                edge.draw_edge(win)
        
    
        if V:
            for vertex in V:
                vertex.draw_vertex(win)
        
        if W:
            for edge in W:
                
                if W[edge].draw_button():
                    W[edge].pressed=not(W[edge].pressed)
                if W[edge].pressed:
                    for e in W:
                        if e!=edge:
                            W[e].pressed=False
                    w_action=True
                    
                if W[edge].text_w=="" and W[edge].pressed==False:
                    W[edge].text_w=str("1")
                    
                    W[edge].cur+=6
                if W[edge].text_w:
                    edge.weight=int(W[edge].text_w)
                    
                    
        if algo_pressed:
            for algorithm in algo_choices:
                if algorithm.draw_button():
                    for al in algos:
                        if al==algorithm:
                            algos[algorithm]=1
                        else:
                            algos[al]=0

        for event in pygame.event.get():
            
            
            if event.type==pygame.KEYDOWN and w_action:
                
                for e in W:
                    if W[e].pressed:
                        if event.key==pygame.K_BACKSPACE and W[e].text_w and W[e].cur>W[e].border-7 : 
                            W[e].cur-=6
                            W[e].text_w=W[e].text_w[:len(W[e].text_w)-1]



                        elif event.key !=pygame.K_BACKSPACE and W[e].cur<W[e].x+W[e].width-14 :
                            
                            if   "0"<=event.unicode<="9" or event.unicode==" ":
                                W[e].text_w+=event.unicode
                                W[e].cur+=6
                        
                        
            if event.type==pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN and actions[add_v]:
                if event.key == pygame.K_UP:
                    adding_vertices(c,V)
                    
            elif event.type==pygame.KEYDOWN and actions[rm_v]:
                if event.key == pygame.K_DOWN:
                    removing_vertices(V,E,W,junk)

            elif event.type==pygame.KEYDOWN and actions[add_e]:
                if event.key == pygame.K_LEFT :
                    pos[0]=pygame.mouse.get_pos()
                    for vertex in V:
                        if distance(vertex.position,pos[0])<=vertex.radius:
                            pos[0]=vertex.position
                            v1=vertex
                            arrow_left= 1
                            break
                    
                if event.key==pygame.K_RIGHT and arrow_left :
                    pos[1]=pygame.mouse.get_pos()
                    for vertex in V:
                        if distance(vertex.position,pos[1])<=vertex.radius:
                            pos[1]=vertex.position
                            v2=vertex
                            if v1!=v2 and v2 not in v1.neighbors:
                                adding_edges(win,E,pos,v1,v2,W,junk,start,directed.text=="Directed")
                                break
                    arrow_left = 0
                    
                    pos=[(0,0),(0,0)]
            elif event.type==pygame.KEYDOWN and actions[rm_e]:
                if event.key == pygame.K_LEFT :
                    pos[0]=pygame.mouse.get_pos()
                    for vertex in V:
                        if distance(vertex.position,pos[0])<=vertex.radius:
                            pos[0]=vertex.position
                            v1=vertex
                            arrow_left= 1
                            break 
                if event.key==pygame.K_RIGHT and arrow_left :
                    pos[1]=pygame.mouse.get_pos()
                    for vertex in V:
                        if distance(vertex.position,pos[1])<=vertex.radius:
                            v2=vertex
                            if v2 in v1.neighbors :
                                removing_edges(E,v1,v2,W,junk,directed.text=="Directed")
                            break
                    arrow_left = 0
                    pos=[(0,0),(0,0)]
                    
                    
            elif event.type==pygame.KEYDOWN and algo_pressed:
                if algos[COLORS] :
                    
                    COLORSS(V,E,win)
                    algos[COLORS]=0
                    break
                elif event.key == pygame.K_LEFT and algos[DFS] :
                    pos[0]=pygame.mouse.get_pos()
                    for vertex in V:
                        if distance(vertex.position,pos[0])<=vertex.radius:
                            v1=vertex
                            dfs(v1,V,E,win)
                            break
                elif event.key == pygame.K_LEFT and algos[BFS] :
                    pos[0]=pygame.mouse.get_pos()
                    for vertex in V:
                        if distance(vertex.position,pos[0])<=vertex.radius:
                            v1=vertex
                            bfs(v1,V,E,win)
                            break
                elif event.type==pygame.KEYDOWN and algos[DIJKSTRA]:
                    if event.key == pygame.K_LEFT :
                        pos[0]=pygame.mouse.get_pos()
                        for vertex in V:
                            if distance(vertex.position,pos[0])<=vertex.radius:
                                pos[0]=vertex.position
                                vertex.make(purple)
                                vertex.draw_vertex(win)
                                pygame.display.update()
                                v1=vertex
                                arrow_left= 1
                                break
                    if event.key==pygame.K_RIGHT and arrow_left:
                        pos[1]=pygame.mouse.get_pos()
                        for vertex in V:
                            if distance(vertex.position,pos[1])<=vertex.radius:
                                pos[1]=vertex.position
                                vertex.make(Periwinkle)
                                vertex.draw_vertex(win)
                                pygame.display.update()
                                v2=vertex
                                if v1!=v2:
                                    delay(1)
                                    vertex.make(turquoise)
                                    vertex.draw_vertex(win)
                                    pygame.display.update()
                                    delay(1)
                                    dijkstra(v1,v2,V,E,win)
                                    break
                        arrow_left = 0
                        pos=[(0,0),(0,0)]

            pygame.display.update()
    pygame.quit()
    
if __name__=="__main__":
    main()


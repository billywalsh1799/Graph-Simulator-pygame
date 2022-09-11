#test11

import pygame
import time
from math import*
#check
pygame.init()
#width,height=1000,780
#width,height=1360,780
#width,height=1600,900
width,height=1800,980
win=pygame.display.set_mode((width,height))


clicked=False
white=255,255,255

black=0,0,0
blue=0,0,255
green=(0,255,0)
orange=(200,215,10) 
light_red=239,48,56
turquoise=64,224,208
beige=234,210,168
gray=(105,105,105)
purple=(159, 43, 104)
Periwinkle=(204, 204, 255)



#font=pygame.font.SysFont('consolas', 20)
def distance(p1,p2):
    d=(p1[0]-p2[0])**2+(p1[1]-p2[1])**2
    return sqrt(d)

def draw_text(txt,pos,color):
    font_obj=pygame.font.SysFont('consolas', 20)
    text_surface_obj = font_obj.render(txt,True,color)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center =pos
    win.blit(text_surface_obj, text_rect_obj)

class button():
    button_col=25,190,225
    click_col=50,150,255
    hover_col=75,225,255
   
    text_col=255,255,255
    width=180
    height=40
    font_size=20
    shading=1
    
    def __init__(self,x,y,text):
        self.x=x
        self.y=y
        self.text=text
    def draw_button(self):
        global clicked
        action=False
        temp=self.text_col
        pos=pygame.mouse.get_pos()
        button_rect=pygame.Rect(self.x,self.y,self.width,self.height)
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                clicked=True            
                if self.shading:
                    pygame.draw.rect(win,self.click_col,button_rect)
                else:
                    self.text_col=gray
                    
                
            elif pygame.mouse.get_pressed()[0]==0 and clicked:
                clicked=False
                action=True
            else:
                if self.shading:
                    pygame.draw.rect(win,self.hover_col,button_rect)
                else:
                    
                    self.text_col=white
        
        else:
            pygame.draw.rect(win,self.button_col,button_rect)
        if self.shading:
            pygame.draw.line(win,white,(self.x,self.y),(self.x+self.width,self.y),2)
            pygame.draw.line(win,white,(self.x,self.y),(self.x,self.y+self.height),2)
            pygame.draw.line(win,black,(self.x,self.y+self.height),(self.x+self.width,self.y+self.height),2)
            pygame.draw.line(win,black,(self.x+self.width,self.y),(self.x+self.width,self.y+self.height),2)
        
        
        font_obj=pygame.font.SysFont('consolas',self.font_size)
        text_img = font_obj.render(self.text,True,self.text_col)
        text_len = text_img.get_width()
        positions =(self.x+(self.width//2)-(text_len//2),self.y+5)
        win.blit(text_img,positions)
        self.text_col=temp
        return action

    
    
    
    
class w_button:
    button_col=black
    hover_col=gray
    click_col=light_red
    width=100
    height=70
    size_e=30
    size_w=25
    #tab=pygame.Rect(x,880,100,70)
    
    def __init__(self,x,y,text_e,text_w):
        self.x=x
        self.y=y
        self.text_e=text_e
        self.text_w=text_w
        self.pressed=False
        pos=x+(w_button.width/2)-8*len(text_w)
        self.border=pos+len(text_w)*14
        self.cur=pos+len(text_w)*14
    def draw_button(self):
        global clicked
        action=False
        pos=pygame.mouse.get_pos()
        button_rect=pygame.Rect(self.x,self.y,self.width,self.height)
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                clicked=True            
                pygame.draw.rect(win,self.click_col,button_rect,3)
                pygame.draw.line(win,self.click_col,(self.x,self.y+self.height//2),(self.x+self.width-1,self.y+self.height//2),3)
                
            elif pygame.mouse.get_pressed()[0]==0 and clicked:
                clicked=False
                action=True
            else:
                pygame.draw.rect(win,self.hover_col,button_rect,3)
                pygame.draw.line(win,self.hover_col,(self.x,self.y+self.height//2),(self.x+self.width-1,self.y+self.height//2),3)
        
        else:
            pygame.draw.rect(win,self.button_col,button_rect,3)
            pygame.draw.line(win,black,(self.x,self.y+self.height//2),(self.x+self.width-1,self.y+self.height//2),3)
        
        
        font1=pygame.font.SysFont('consolas',self.size_e)
        font2=pygame.font.SysFont('consolas',self.size_w)
        
        
        
        edge= font1.render(self.text_e,True,black)
        edge_len = edge.get_width()
        positions =(self.x+(self.width//2)-(edge_len//2),self.y+5)
        win.blit(edge,positions)
        
        weight=font2.render(self.text_w,True,black)
        position=(self.x+(self.width/2)-8*len(self.text_w),self.y+(3/4)*self.height-12)
        win.blit(weight,position)
        if self.pressed:
            pygame.draw.line(win,black,(self.cur,position[1]),(self.cur,position[1]+23))
        
        return action
    
    
    
    
    
    
    
    

    
    
    


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
        draw_text(str(self.id),self.position,black)
    def __str__(self):
        return str(self.id)
    def make(self,c):
        self.color=c
        
class edge:
    def __init__(self,pos,extents,w=1): 
        self.position=pos
        self.extents=extents
        self.weight=w
        self.color=black
    def make_white(self):
        self.color=white
    def make_black(self):
        self.color=black
    def make_Periwinkle(self):
        self.color=Periwinkle
    
    def draw_edge(self,win):
        pygame.draw.line(win,self.color,self.position[0],self.position[1],5)
    def __str__(self):
        return str(self.extents[0])+"-"+str(self.extents[1])



def adding_vertices(win,counter,V): 
    pos=pygame.mouse.get_pos()
    #borders
    #pygame.draw.line(win,black,(1575,0),(1575,850),3)
    #pygame.draw.line(win,black,(0,850),(1575,850),3)
    if pos[0]<1545 and pos[1]<820:
        v=vertex(pos,counter[0])
        V.add(v)
        counter[0]+=1
    
def removing_vertices(win,V,c,E,W,junk):
    pygame.event.pump()
    pos=pygame.mouse.get_pos()
    l=[]
    for vertex in V:
        if distance(vertex.position,pos)<=vertex.radius:
            pygame.event.pump()
            #V.remove(vertex)
            #e=edge(pos,(v1,v2))
            for e in E:
                if vertex in e.extents:
                    #V.remove(vertex)
                    #E.remove(e)
                    l.append(e)
            for i in l:
                
                junk.append(W[i].x)
                del W[i]
                E.remove(i)
                
                
            for j in vertex.neighbors:
                j.neighbors.remove(vertex)
            
            V.remove(vertex)
            #c[0]-=1
            break
def adding_edges(win,E,pos,v1,v2,W,junk,start):
    v1.neighbors.add(v2)
    v2.neighbors.add(v1)
    v2.deg+=1
    v1.deg+=1
    
    #pygame.time.delay(2000)
    
    #v1.make_blue()
    #v1.draw_vertex(win)
    #pygame.display.update()
    
    #pygame.time.delay(2000)
    #v2.make_blue()
    #v2.draw_vertex(win)
    #pygame.display.update()
    
    e=edge(pos,(v1,v2))
    E.add(e)
    
    
    if junk:
        x=junk.pop(0)
        #tab=pygame.Rect(x,880,100,70)
        #pygame.draw.rect(win,black,tab,3)
        tab=w_button(x,880,str(e),str(e.weight))
        W[e]=tab
    else:
    
        tab=w_button(start[0],880,str(e),str(e.weight))
        start[0]+=101
        W[e]=tab
    
    
    
    
    
    
    
    #pygame.time.delay(2000)
    #pygame.draw.line(win,black,pos[0],pos[1])
    #v1.draw_vertex(win)
    #v2.draw_vertex(win)
    print("yo")
    


def removing_edges(win,E,v1,v2,W,junk,start):
    v1.neighbors.remove(v2)
    v2.neighbors.remove(v1)
    v2.deg-=1
    v1.deg-=1
    for e in E:
        if e.position==[v1.position,v2.position] or e.position==[v2.position,v1.position]:
            E.remove(e)
            junk.append(W[e].x)
            del W[e]
            break
    #E.remove(edge)
def mini(path):
    x=list(path.keys())[0]
    y=path[x][0]
    for v in path:
        if path[v][0]<y:
            y=path[v][0]
            x=v
    return x
            
def delay(t):
    
    start=time.time()
    while 1:
        end=time.time()
        if end-start>t:
            break
        pygame.event.pump()
            
   
    

            
            
def dijkstra(s,d,V,E,win):
        visited={i:0 for i in V}
        path={i:[float("inf"),""] for i in V}
        path[s]=[0,""]
        temp={s:[0,""]}
        #mini function must change
        while temp:
            key=mini(temp)
            used_edges=set()
            used_vertices=set()
            #change v color maybbe key with another color
            key.make_green()
            key.draw_vertex(win)
            pygame.display.update()
            delay(1)
            
            visited[key]=1
            for v in key.neighbors:
                #change edge(key,v) color
                if visited[v]:
                    continue
                #search for the edge to color it
                for edge in E:
                    if edge.extents==(key,v) or edge.extents==(v,key):
                        tempo=edge
                        used_edges.add(edge)
                        used_vertices.add(v)
                        edge.make_white()
                        edge.draw_edge(win)
                        key.draw_vertex(win)
                        v.draw_vertex(win)
                        #redraw_verteces
                        pygame.display.update()
                        delay(1)
                        break
                
                
                x=path[v][0]
                y=path[key][0]+tempo.weight #fix the weight function tempo?
                if  y<x:
                    path[v]=[y,key]
                    temp[v]=[y,key]
            
            delay(1)
            
            
            
            for edge in used_edges:
                edge.make_black()
                edge.draw_edge(win)
            for vertex in used_vertices:
                vertex.make_turqoise()
                vertex.draw_vertex(win)
            key.make_blue()
            key.draw_vertex(win) 
                
            
            
            pygame.display.update()
            if key==d:
                break
            del temp[key]
        
        #color used edges and verticeswith Periwinkle
        #test result
        chemin=[d]
        current=d
        while current!=s:
            current=path[current][1]
            chemin.append(current)
        used_edges=set()
        used_vertices=set()
        for i in range(len(chemin)-1,0,-1):
            #rint(chemin[i],chemin[i-1])
            for edge in E:
                if edge.extents==(chemin[i],chemin[i-1]) or edge.extents==(chemin[i-1],chemin[i]):
                    tempo=edge
                    used_edges.add(edge)
                    used_vertices.add(v)
                    edge.make_Periwinkle()
                    edge.draw_edge(win)
                    
                    chemin[i-1].make_Periwinkle()
                    chemin[i-1].draw_vertex(win)
                    
                    chemin[i].make_Periwinkle()
                    chemin[i].draw_vertex(win)
                    
                    #redraw_verteces
                    pygame.display.update()
                    delay(1)
                    break
            
        
        
        
        
        
        delay(2)
        
        for edge in E:
            edge.make_black()
            edge.draw_edge(win)
        
        for vertex in V:
            vertex.make_turqoise()
            vertex.draw_vertex(win)
        
        
        pygame.display.update()
        pygame.event.pump()
        
        
            
        
        
def shortest_path(self,s,d):
    path=self.dijkstra(s,d)
    if path[d][1]=="":
        print("There is no path from {} to {}".format(s,d))
        return
    chemin=[str(d)]
    current=d
    while current!=s:
        current=path[current][1]
        chemin.append(str(current))
    result=chemin.pop()
    for i in range(len(chemin)):
        result+=" -> "+chemin.pop()
    return result

def temptext(stack):
    recta=pygame.Rect(0,855,1500,300)
    pygame.draw.rect(win,beige,recta)
    #draw_text(txt,(100,70),beige)
    pygame.display.update()
    
    txt=''
    for x in stack : 
            txt=txt+'  '+str(x.id) 
    draw_text(txt,(750,890),black)
    pygame.display.update()
    delay(0.3)

        
def dfs(v1,V,E,win):
    
        
        
        visited={v1}
        unvisited={edge:0 for edge in E}
        self_visited={v:False for v in V}
        self_visited[v1]=True
        stack=[v1]
        
        def color_edges(E):
            for edge in E:
                if edge.extents[0].color==light_red and edge.extents[1].color==light_red and unvisited[edge]==0:
                    edge.make_white()
                    edge.draw_edge(win)
                    edge.extents[0].draw_vertex(win)
                    edge.extents[1].draw_vertex(win)
                    unvisited[edge]=1
                    #pygame.time.Clock()
                    #pygame.time.wait(500)
                    delay(0.5)
                    pygame.time.Clock().tick(fps)
                    #draw only unvisited edges and vertices to not waste time
                    #draw vertices too
        

        v1.make_green()
        v1.draw_vertex(win)
        pygame.display.update()
        #pygame.time.delay(1000)
        delay(1)
        pygame.time.Clock().tick(fps)

        
        v1.make_blue()
        v1.draw_vertex(win)
        pygame.display.update()
        #pygame.time.wait(1000)
        temptext(stack)
        delay(0.5)
        
        #must change edges color each time
        
        #stack+=v1.neighbors
        
        for vertex in v1.neighbors:
            stack.append(vertex) 
            temptext(stack)
        
        #**********************************
        while stack!=[]:
            #add for event and quit
            x=stack.pop()
            delay(0.5)
            temptext(stack)
            
            visited.add(x)
            if self_visited[x]==False:
                x.make_green()
                x.draw_vertex(win)
                pygame.display.update()
                delay(0.5)
                
                #pygame.time.wait(500)
                
                pygame.time.Clock().tick(fps)


                x.make_blue()
                x.draw_vertex(win)
                delay(0.5)
                #pygame.time.delay(1000)
                #change edge color here for edge in E in edge.extents[0] or 1 color red than change it
                color_edges(E)
                
                pygame.display.update()
                #pygame.time.wait(500)
                delay(0.5)
                pygame.time.Clock().tick(fps)
                
                
                #stack+=x.neighbors
                for vertex in x.neighbors:
                    stack.append(vertex)
                    temptext(stack)
                    delay(1)
                    
                self_visited[x]=True
        
        temptext(stack) 
        #pygame.time.wait(1000)
        delay(0.5)
        pygame.time.Clock().tick(fps)
        #or create a reset button
        #return visited
        #redraw only visited edges and vertices to avoid stutter
        for vertex in V:
            vertex.make_turqoise()
            vertex.draw_vertex(win)
        for edge in E:
            edge.make_black()
            edge.draw_edge(win)
        
        pygame.display.update()
        pygame.event.pump()
        print("dfs done")
            

#bfs and find a solution for weights


def bfs(v1,V,E,win):
    
        
        visited={v1}
        unvisited={edge:0 for edge in E}
        self_visited={v:False for v in V}
        self_visited[v1]=True
        stack=[v1]
        def color_edges(E):
            for edge in E:
                if edge.extents[0].color==light_red and edge.extents[1].color==light_red and unvisited[edge]==0:
                    edge.make_white()
                    edge.draw_edge(win)
                    edge.extents[0].draw_vertex(win)
                    edge.extents[1].draw_vertex(win)
                    unvisited[edge]=1
                    #pygame.time.Clock()
                    #pygame.time.wait(500)
                    delay(0.5)
                    pygame.time.Clock().tick(fps)
                    #draw only unvisited edges and vertices to not waste time
                    #draw vertices too
        

        v1.make_green()
        v1.draw_vertex(win)
        pygame.display.update()
        #pygame.time.delay(1000)
        temptext(stack)
        delay(1)
        pygame.time.Clock().tick(fps)

        
        v1.make_blue()
        v1.draw_vertex(win)
        pygame.display.update()
        #pygame.time.wait(1000)
        temptext(stack)
        delay(0.5)
        
        #must change edges color each time
        
        #stack+=v1.neighbors
        for vertex in v1.neighbors:
            stack.append(vertex)
            temptext(stack)
        while stack!=[]:
            x=stack.pop(0)
            visited.add(x)
            temptext(stack)
            if self_visited[x]==False:
                x.make_green()
                x.draw_vertex(win)
                pygame.display.update()
                #pygame.time.wait(500)
                delay(0.5)
                pygame.time.Clock().tick(fps)


                x.make_blue()
                x.draw_vertex(win)
                #pygame.time.delay(1000)
                #change edge color here for edge in E in edge.extents[0] or 1 color red than change it
                color_edges(E)
                
                pygame.display.update()
                #pygame.time.wait(500)
                delay(0.5)
                pygame.time.Clock().tick(fps)
                
                
                #stack+=x.neighbors
                for vertex in x.neighbors:
                    stack.append(vertex)
                    temptext(stack)
                self_visited[x]=True
                
        #pygame.time.wait(1000)
        temptext(stack)
        delay(0.5)
        
        pygame.time.Clock().tick(fps)
        #or create a reset button
        #return visited
        #redraw only visited edges and vertices to avoid stutter
        for vertex in V:
            vertex.make_turqoise()
            vertex.draw_vertex(win)
        for edge in E:
            edge.make_black()
            edge.draw_edge(win)
        
        pygame.display.update()
        pygame.event.pump()
        print("bfs done")

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

                #pygame.time.wait(500)
                delay(0.6)
                pygame.time.Clock().tick(fps)


                
                
               
                
                for j in range(i+1,len(l)):
                    if colored[l[j]]==False and (not coloredneigh(l[j],colored,num))  : 
                        
                        colored[l[j]]=num
                        l[j].make(colors[num])
                        l[j].draw_vertex(win)
                        pygame.display.update()
                        #pygame.time.wait(500)
                        delay(0.5)
                        pygame.time.Clock().tick(fps)
                num+=1
                delay(2)
        for i in V :
            i.make(turquoise)
        print('coloring done')




                





        

            












s=0,0
e=500,500
fps=60


#font_obj = pygame.font.Font('freesansbold.ttf', 50)



def main():
    #star x was 40
    start=[20,880]
    V=set()
    E=set()
    W={} #key (v1,2) value associated edge
    counter=[0]
    positions={}
    edges={} #key(v1,v2) value assosiated edge
    junk=[]
    
    beige=234,210,168
    e=0
    clock=pygame.time.Clock()
    run=True
    #win.fill(beige)
    click=False
    algo_pressed=False
    
   
    
    add_v=button(1600,100,"add vertex")
    rm_v=button(1600,200,"remove vertex")
    add_e=button(1600,300,"add edge")
    rm_e=button(1600,400,"remove edge")
    algo=button(1600,500,"Algorithms")
    
    menu={add_v,rm_v,add_e,rm_e,algo}


    DFS=button(1660,600,"DFS")
    DFS.height=22
    DFS.width=45
    DFS.text_col=black
    DFS.button_col=beige
    DFS.shading=0

    BFS=button(1660,650,"BFS")
    BFS.height=22
    BFS.width=45
    BFS.button_col=beige
    BFS.text_col=black
    BFS.shading=0


    DIJKSTRA=button(1645,700,"DIJKSTRA")
    DIJKSTRA.height=22
    DIJKSTRA.width=85
    DIJKSTRA.button_col=beige
    DIJKSTRA.text_col=black
    DIJKSTRA.shading=0
    #modify contructor for button class
    
    
    COLORS=button(1660,750,"COLORS")
    COLORS.height=22
    COLORS.width=45
    COLORS.button_col=beige
    COLORS.text_col=black
    COLORS.shading=0
    
    algo_choices={DFS,BFS,DIJKSTRA,COLORS}

    
    user_input=""
    
    c=[0]
    test=False
    q=False
    pos=[(0,0),(0,0)]
    actions={add_v:0,rm_v:0,add_e:0,rm_e:0,algo:0}
    algos={DFS:0,BFS:0,DIJKSTRA:0,COLORS:0}
    arrow_left = 0
    
    #enter an edge case to test it with weights already defined like vid

    #whenever a button is pressed action[button]=1 action is only resetted when you press another button one action at a time"
    #make vertex glow by changing color  a lot of time to create motion illusion
    
    
    w_action=False
    #text_len = text_img.get_width()
    cur=35
    while run:
        clock.tick(fps)
        win.fill(beige)
        #start=400,100
        #pygame.draw.line(win,black,(1040,0),(1040,644),3)
        #pygame.draw.line(win,black,(0,644),(1040,644),3)
        
        #borders
        pygame.draw.line(win,black,(1575,0),(1575,850),3)
        pygame.draw.line(win,black,(0,850),(1575,850),3)
        
        #pygame.draw.line(win,black,(cur,500),(cur,520)) odl curser
        """
        pygame.draw.line(win,black,(cur,105-11),(cur,105-11+20))
        font_obj=pygame.font.SysFont('consolas',20)
        edge_weight= font_obj.render(user_input,True,black)
        z =35,(105-11)
        win.blit(edge_weight,z)"""
        
        
        
        """
        font_obj=pygame.font.SysFont('consolas',30)
        edge_name= font_obj.render("0-1",True,black)
        text_len = edge_name.get_width()
        positions =(30+(200//2)-(text_len//2),30+5)
        win.blit(edge_name,positions)"""
        
        """
        table=pygame.Rect(30, 30, 150, 100)
        pygame.draw.line(win,black,(30,80),(229,80),3)
        pygame.draw.rect(win,black,table ,3)"""
        
        
        
        
        
        
        #positions =(self.x+(self.width//2)-(text_len//2),self.y+5)
        
        #win.blit(text_img,(500,500))
        
        
        
        
        
        
        #pygame.draw.rect(win,black,tab,3)
        #pygame.draw.rect(win,black,tab1,3)
        
        
        
        #hovering test
        
        
        
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
                
                
                
        if E:
            for edge in E:
                edge.draw_edge(win)
        
    
        if V:
            for vertex in V:
                vertex.draw_vertex(win)
        
        if W:
            for edge in W:
                #pygame.draw.rect(win,black,W[edge],3)
                if W[edge].draw_button():
                    W[edge].pressed=not(W[edge].pressed)
                    print("yes")
                if W[edge].pressed:
                    for e in W:
                        if e!=edge:
                            W[e].pressed=False
                    w_action=True
                    """
                    table=pygame.Rect(30, 30, 150, 100)
                    pygame.draw.line(win,black,(30,80),(229,80),3)
                    pygame.draw.rect(win,black,table ,3)
                    
                    pygame.draw.line(win,black,(cur,105-11),(cur,105-11+20))
                    font_obj=pygame.font.SysFont('consolas',20)
                    edge_weight= font_obj.render(user_input,True,black)
                    z =35,(105-11)
                    win.blit(edge_weight,z)
                    
                    
                    font_obj=pygame.font.SysFont('consolas',30)
                    edge_name= font_obj.render("0-1",True,black)
                    text_len = edge_name.get_width()
                    positions =(30+(200//2)-(text_len//2),30+5)
                    win.blit(edge_name,positions)"""
                    #cursur test
                
                if W[edge].text_w=="" and W[edge].pressed==False:
                    W[edge].text_w=str("1")
                    #delay(0.1)
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
                            #make it handle only numeric
                            if   "0"<=event.unicode<="9" or event.unicode==" ":
                                W[e].text_w+=event.unicode
                                W[e].cur+=6
                        
                        
                    
                    
                    
                    
                    
                    
                """
        if event.key==pygame.K_BACKSPACE and user_input  :
            cur-=11
            user_input=user_input[:len(user_input)-1]



        elif event.key !=pygame.K_BACKSPACE and cur<(35+17*11):
            #make it handle only numeric
            if   "0"<=event.unicode<="9" or event.unicode==" ":
                user_input+=event.unicode
                cur+=11"""
            
                

       
                
                #else key!=backspace
            
            if event.type==pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN and actions[add_v]:
                if event.key == pygame.K_UP:
                    adding_vertices(win,c,V)
                    
            elif event.type==pygame.KEYDOWN and actions[rm_v]:
                if event.key == pygame.K_DOWN:
                    removing_vertices(win,V,c,E,W,junk)

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
                            if v1!=v2:
                                adding_edges(win,E,pos,v1,v2,W,junk,start)
                                
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
                    #arrow_left= 1
                    
                if event.key==pygame.K_RIGHT and arrow_left :
                    pos[1]=pygame.mouse.get_pos()
                    for vertex in V:
                        if distance(vertex.position,pos[1])<=vertex.radius:
                            v2=vertex
                            removing_edges(win,E,v1,v2,W,junk,start)
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
                    """
                    #try at first single source dijkstra than copy add edge arrow 
                    pos[0]=pygame.mouse.get_pos()
                    for vertex in V:
                        if distance(vertex.position,pos[0])<=vertex.radius:
                            v1=vertex
                            dijkstra(v1,V,E,win)
                            break"""
                    if event.key == pygame.K_LEFT :
                        pos[0]=pygame.mouse.get_pos()
                        for vertex in V:
                            if distance(vertex.position,pos[0])<=vertex.radius:
                                pos[0]=vertex.position
                                print("yoooooo111111")
                                vertex.make_purple()
                                vertex.draw_vertex(win)
                                pygame.display.update()
                                
                                v1=vertex
                                arrow_left= 1
                                break
                    if event.key==pygame.K_RIGHT and arrow_left:
                        pos[1]=pygame.mouse.get_pos()
                        print("yoooooo2222222")
                        for vertex in V:
                            if distance(vertex.position,pos[1])<=vertex.radius:
                                pos[1]=vertex.position
                                
                                vertex.make_Periwinkle()
                                vertex.draw_vertex(win)
                                pygame.display.update()
                                
                                v2=vertex
                                if v1!=v2:
                                    delay(1)
                                    vertex.make_turqoise()
                                    vertex.draw_vertex(win)
                                    pygame.display.update()
                                    delay(1)
                                    dijkstra(v1,v2,V,E,win)
                                    break
                        arrow_left = 0
                        pos=[(0,0),(0,0)]

                
                    
                            
                
            
            
    
                
                
            
                #print(pygame.key.name(event.key))
                
            #if event.type == pygame.MOUSEWHEEL:
                
            #if event.type==pygame.MOUSEBUTTONUP and test:
                
                
                #print("entourage")
                
            pygame.display.update()
            
    
    #print("width=",text_len)  
    
    
    pygame.quit()
    print(len(V))
    for i in V:
        print(i)  
    for e in E:
        print(e,"weight=",e.weight) 
    print(junk)
    print(w_action)
                
            
    
    
    
if __name__=="__main__":
    main()


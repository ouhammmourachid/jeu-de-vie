# here we had import librory tkinter and numpy

import tkinter as tk
import numpy as np


# we create our variable that we will need in our game

M=[[0 for i in range(65)] for j in range(46)]
gen=0
a=False

# function voisin give us all the adjacent squares

def voisin(M,C):
    m=len(M)
    if C==[0,0]:
        return [[1,0],[1,1],[0,1]]
    elif C==[0,m-1]:
        return [[1,m-1],[0,m-2],[1,m-2]]
    elif C==[m-1,m-1]:
        return [[m-1,m-2],[m-2,m-1],[m-2,m-2]]
    elif C==[m-1,0]:
        return [[m-2,0],[m-1,1],[m-2,1]]
    elif C[0]==0:
        return [[0,C[1]+1],[0,C[0]-1],[1,C[1]],[1,C[1]-1],[1,C[1]+1]]
    elif C[0]==m-1:
        return [[m-1,C[1]-1],[m-1,C[1]+1],[m-2,C[1]],[m-2,C[1]-1],[m-2,C[1]+1]]
    elif C[1]==0:
        return [[C[0],1],[C[0]+1,1],[C[0]-1,1],[C[0]+1,0],[C[0]-1,0]]
    elif C[1]==m-1:
        return [[C[0],m-2],[C[0]+1,m-2],[C[0]-1,m-2],[C[0]+1,m-1],[C[0]-1,m-1]]
    else:
        return [[C[0]-1,C[1]],[C[0]-1,C[1]-1],[C[0]-1,C[1]+1],[C[0],C[1]+1],[C[0],C[1]-1],[C[0]+1,C[1]],[C[0]+1,C[1]-1],[C[0]+1,C[1]+1]]


# here we programe the first rule in jeu de vie 

def rule_1(M):
    change=[]
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j]==0:
                s=0
                for voi in voisin(M,[i,j]):
                    if M[voi[0]][voi[1]]==1:
                        s+=1
                if  s==3:
                    change+=[[i,j]]
    return change


# here we programe the second rule in jeu de vie
def rule_2(M):
    change=[]
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j]==1:
                s=0
                for voi in voisin(M,[i,j]):
                    if M[voi[0]][voi[1]]==1:
                        s+=1
                if s!=2 and s!=3:
                    change+=[[i,j]]
    return change


# here we programe the main function of the game that return the matrix 

def jeu_de_vie(M):
    change1=rule_1(M)
    change2=rule_2(M)
    for i in range(len(M)):
        for j in range(len(M)):
            if [i,j] in change1:
                M[i][j]=1
            if [i,j] in change2:
                M[i][j]=0
    return M


# the class of the buttom we will use soon with tkinter code

class buton(tk.Button):
    all=[]
    def __init__(self,x:int,y:int):
        tk.Button.__init__(self,bg='white',command=self.switch_color)
        self.place(x=x*13,y=y*13,width=15,height=15)
        self.x=x
        self.y=y
        buton.all.append(self)
    def switch_color(self):
        if M[self.y][self.x]==0:
            self.config(bg="red")
            M[self.y][self.x]=1
        else:
            self.config(bg="white")
            M[self.y][self.x]=0


# here the function is linked to yhe button reset that reset all the bord

def reset():
    global M
    global gen
    for i in buton.all:
        i.config(bg="white")
        M[i.y][i.x]=0
    buton.red=[]
    stop()
    gen=0
    ng.configure(text="0")


# here the fuction is respond of the cell that will die and whose who will live

def step_by_step():
    global M 
    global gen
    M=jeu_de_vie(M)
    for i in buton.all:
        if M[i.y][i.x]==0:
            i.config(bg="white")
        else:
            i.config(bg="red")
        i.update()
    gen+=1
    ng.configure(text=str(gen))
    ng.update()


# animation

def animation():
    global M
    global a
    a=True
    while a:
        for i in range(5):
            step_by_step()


# to stop the animation 

def stop():
    global a
    a=False


# here we define the tkinter window

window = tk.Tk()
window.title("jeu de vie")
window.config(width=1000,height=600)
window.resizable(False, False)
window.config(bg="white")


# here we define the start and reset and step_by_step and stop button

Butt=tk.Button(window,text="start",command=animation)
Butt.place(x=900,y=100)
Butt1=tk.Button(window,text="reset",command=reset)
Butt1.place(x=900,y=200)
Butt2=tk.Button(window,text="step_by_step",command=step_by_step)
Butt2.place(x=880,y=300)
Butt2=tk.Button(window,text="stop",command=stop)
Butt2.place(x=900,y=400)


# here we define all cell button

for i in range(65):
    for j in range(46):
        buton(i,j)


# here we define some labels for geneartion number

g=tk.Label(text="generation:",bg="white")
g.place(x=880,y=550)
ng=tk.Label(text="0",bg="white",fg="red")
ng.place(x=890,y=570)


window.mainloop()

# fin

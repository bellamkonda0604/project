from cmu_112_graphics import *
from random import*
from tkinter import*
import random
import time
canvas_width=800
canvas_height=400
import time
import tkinter as tk
import basic_graphics
display = 0

time_start = time.time()
#Do function stuff

# def appStarted(app):
#     app.cx = app.width/2
#     app.cy = app.height/2
#     app.r = 40

# def timerFired(app):
#     app.cx -= 10
#     if (app.cx + app.r <= 0):
#         app.cx = app.width + app.r

# def redrawAll(app, canvas):
#     canvas.create_rectangle(app.cy+app.r, app.cx+app.r,app.cy-app.r, app.cx-app.r,fill='darkGreen')

# runApp(width=600, height=800)
root = Tk()

root.title('TRY TO ESCAPE')
root.geometry("300x400")
w=300
h=400
x=w//2
y=h//2
my_canvas=Canvas(root,width=w, height=h,bg="#c2b280")
my_canvas.pack(pady=20)
score_text=my_canvas.create_text(115,0,anchor='nw',font=('Oswald',15,'bold'),fill='black',text='score='+str(0))

speed=500
interval=4000

obst=[]
start = True
aa=10
score=0

def create_obs():
    global aa
    if aa!=1:
        my_canvas.itemconfigure(score_text,text='score='+str(int(time.time() - time_start)))
        x=randrange(1,4)
        color_cycle = random.choice(('red', 'yellow', 'green','white','mediumvioletred', 'aqua','black'))
        # y=40
        l1=my_canvas.create_rectangle((x-1)*100,20,x*100,70,fill=color_cycle)
        obst.append(l1)
        root.after(interval,create_obs)
   
def move_obs():
    global aa
    if aa!=1:
        global speed
        speed = speed + 30
        my_canvas.itemconfigure(score_text,text='score='+str(int(time.time() - time_start)))
        for obs in obst:
            my_canvas.itemconfigure(score_text,text='score='+str(int(time.time() - time_start)))
            (x,y,x2,y2) = my_canvas.coords(obs)
            my_canvas.move(obs,0,50)
            if y2 > canvas_height:
                obst.remove(obs)
        root.after(speed,move_obs)


my_circle=my_canvas.create_oval(x-40,y+160,x+40,y+90,fill="black")
my_canvas.create_line(100,20,100,400)
direct=2
my_canvas.create_line(200,20,200,400)
def left(event):
    x=-(w//3)
    global direct
    y=0
    if direct>1:
        direct=direct-1
        my_canvas.move(my_circle,-100,y)
    
def right(event):
    global direct
    x=w//3
    y=0
    if direct<3:
        direct = direct + 1 
        my_canvas.move(my_circle,x,y)

def crash():
    global aa,display
    if(aa!=1):
        my_canvas.itemconfigure(score_text,text='score='+str(int(time.time() - time_start)))
        for obs in obst:
            (x,y,x2,y2)=my_canvas.coords(obs)
            my_canvas.itemconfigure(score_text,text='score='+str(int(time.time() - time_start)))
            if y2 >= 300 and x2//100 == direct and y<370:
                aa=1
                obst.clear()
                display=my_canvas.create_text(100,100,anchor='nw',font=('Oswald',20,'bold'),fill='black',text=' GAME \n OVER')
                return

        root.after(100,crash)


def Opening():
    global time_start,my_circle,score_text,my_canvas,direct
    time_start = time.time()
    global speed
    speed = 500
    global aa
    aa=0
    obst.clear()
    my_canvas.delete("all")
    my_circle=my_canvas.create_oval(x-40,y+160,x+40,y+90,fill="black")
    my_canvas.create_line(100,30,100,400)
    direct=2
    score_text=my_canvas.create_text(115,0,anchor='nw',font=('Oswald',15,'bold'),fill='black',text='score='+str(0))
    my_canvas.create_line(200,30,200,400)
    root.bind("<Left>",left)
    root.bind("<Right>",right)
    root.after(1000,create_obs)
    root.after(1000,move_obs)
    root.after(1000,crash)



    
root.bind("<Left>",left)
root.bind("<Right>",right)
root.after(1000,create_obs)
root.after(1000,move_obs)
root.after(1000,crash)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="New",)
filemenu.add_command(label="Play", command=Opening)

filemenu.add_separator()

filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="Home", menu=filemenu)
root.config(menu=menubar)
root.mainloop()
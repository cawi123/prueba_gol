#nombre:Michael Cardenas
#fecha:04/01/2017

#Prueba dos
import time 
from tkinter import *
tk = Tk()
x=200
y=200

#Creamos la ventana 
canvas = Canvas(tk, width=700 ,height=300)
canvas.pack()
#El archivo de la imagen 
image=PhotoImage(file="balon.gif")
my_image=PhotoImage(file="arco.gif")
images=PhotoImage(file="gol.gif")
#Creamos la imagen en la ventana 
canvas.create_image(0,0,anchor=NW,image=image)
#creamos la otra imagen en la misma ventana
canvas.create_image(300,0,anchor=NW,image=my_image)
#creamos la funcion del movimiento DEL balon


def mover(move):
    b=-5
    c=300
    print("x , y")
    if move.keysym == 'A':
        global x
        global y
        x=x-3
        
        print(x,y)
        canvas.move(1,-5,0)
            
    elif move.keysym == 'D':
        global x
        global y
        x=x+3
        print(x,y)
        canvas.move(1,5,0)
    if(x>365):
        canvas.create_image(300,0,anchor=NW,image=images)

     
canvas.bind_all('<KeyPress-A>', mover)
canvas.bind_all('<KeyPress-D>', mover)


tk.mainloop()

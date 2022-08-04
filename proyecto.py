"""import tkinter
from tkinter import *
from pynput import keyboard as kb

ventana = Tk()
ventana.title("Primera Ventana") #Cambiar el nombre de la ventana
ventana.geometry("520x480") #Configurar tamaño
#ventana.iconbitmap("form.ico") #Cambiar el icono

fondo=tkinter.PhotoImage(file="background.gif")
lbl_fondo=tkinter.Label(ventana, image=fondo).place(x=0,y=0)
boton=tkinter.Button(ventana,text="picame").pack()

ventana.mainloop()


"""

import tkinter as tk
from tkinter import Canvas
ventana=tk.Tk()

canvas=Canvas(ventana,width=460,height=480)
canvas.pack()

canvas.create_line(10,20,100,150, fill='#FF0000', width=3)
ventana.mainloop()


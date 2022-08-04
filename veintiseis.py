import tkinter
from tkinter import *

raiz= Tk()
raiz.title('mi primera ventana')
raiz.resizable(False,True)
raiz.geometry("700x700")
raiz.config(bg="green")
titulo=Label(raiz,text="hola",bg="blue",fg="white").pack()
imagen=PhotoImage(file="lenna.png")
photo=Label(raiz,image=imagen,width=200,height=100).pack()
input=tkinter.Entry().pack()
def saludar():
        print('hola',input.get)
boton=tkinter.Button(text="da click", command=saludar).pack()







raiz.mainloop()

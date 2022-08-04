import tkinter
from tkinter import *
from math import *
 
#VISUALIZAR LA OPERACION EN LA PANTALLA
val=[]
def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)
    """val.append(num)
    print(val)"""

#CÁLCULO Y MUESTRA DE RESULTADOS.
def resultado():
    result=tkinter.Label(ventana,text="").place(x=185,y=400)
    array=[]
    p="p","q","r"
    pv=[]
    val=""
    val=val+input_text.get()
    for i in val:
        array.append(i)
        if i in p:
            pv.append(i)
            print(f"valores primiticos {pv}")
    print(array)
    if len(array)>=2:
        result=tkinter.Label(ventana,text="Tabla").place(x=185,y=400)
        table=tkinter.Label(ventana,text=val).place(x=185,y=440)
    else:
        result=tkinter.Label(ventana,text="").destroy()
    input_text.set("0")

#LIMPIEZA DE PANTALLA.
def clear():
    global operador
    operador=("")
    input_text.set("0")

 
ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600")
ventana.configure(background="SkyBlue4")
color_boton=("gray77")
 
ancho_boton=11
alto_boton=3
input_text=StringVar()
operador=""
 
Salida=Entry(ventana,font=('arial',20,'bold'),width=22,
textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right")
Salida.place(x=10,y=60)
 
#AÑADIR BOTONES.
#CREAMOS NUESTROS BOTONES
Button(ventana,text="p",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("p")).place(x=17,y=180)
Button(ventana,text="q",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("q")).place(x=107,y=180)
Button(ventana,text="r",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("r")).place(x=197,y=180)
Button(ventana,text="^",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("^")).place(x=197,y=240)
Button(ventana,text="~",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("~")).place(x=17,y=240)
Button(ventana,text="v",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("v")).place(x=107,y=240)
Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=290,y=180)
Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=290,y=240)
Button(ventana,text="AC",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:clear()).place(x=197,y=300)
Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:resultado()).place(x=290,y=300)

clear()
 
ventana.mainloop()

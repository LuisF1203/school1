from tkinter import *

def comandos():
    ventana=Tk()
    ventana.title("Comandos de voz")
    ventana.resizable(False,False)
    ventana.geometry("300x130")
    ventana.config(bg="#b10404")
    lista_comandos=Listbox(ventana, width=30, height=4, bg="#b10404",fg="#fefefe",font=("Comic Sans MS",10))
    lista_comandos.insert(0,"1- Videos de calculo / programacion")
    lista_comandos.insert(1,"2- Abrir documentacion python")
    lista_comandos.insert(2,"3- Calcular")
    lista_comandos.insert(3,"4- Mostrar libro")
    lista_comandos.place(x=20, y=30)

def asistente():
    return 0
raiz=Tk()
raiz.title("Asistente virtual")
#raiz.resizable(False,False)
#raiz.geometry("500x500")
#menu
Menu_principal=Menu(raiz) #barra de menu
menu_comandos=Menu(Menu_principal)#menu
menu_comandos.add_command(label="Comandos de voz", command=comandos) #comando de menu
menu_comandos.add_separator()
menu_comandos.add_command(label="Salir", command=raiz.destroy) #comando de menu
Menu_principal.add_cascade(label="Opciones",menu=menu_comandos)#agrega los menus en la barra de menu
raiz.config(menu=Menu_principal)

#imagenes fondos

#imprimir rultados de escuaciones
texto1=Text(raiz, bg="#b10404",fg="#fefefe", font=("Comic Sans MS", 10))
texto1.place(x=280,y=350, width=300, height=50)
Button(raiz, command=asistente, text="Presiona para iniciar",fg="#fefefe",bg="#b10404",font=("Comic Sans MS", 12) ).place(x=350,y=300)
raiz.mainloop()

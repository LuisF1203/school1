import tkinter
import openpyxl
import tkinter as tk
import getpass
import os
from tkinter import filedialog
from tkinter import *
PcUser=str(getpass.getuser())

ventana=tk.Tk()
ventana.geometry('500x700')
ventana.title('proyecto python')
ventana.iconbitmap('img\Capa2.ico')

etiqueta=tkinter.Label(ventana,text="Proyecto Python",bg="#5B9AFF")
etiqueta.pack(side=tkinter.TOP,fill=tkinter.X)
login=tkinter.Label(ventana,text="Iniciar Sesión",pady=40)
mystr = StringVar()
mystr.set('Selecciona el excel')

def seleccionar():
    global file_selected
    global ruta2

    ruta2.destroy()
    root = Tk()
    root.withdraw()
    filetypes = (
        ('Excel files', '*.xlsx'),
    )
    file_selected = filedialog.askopenfile(filetypes=filetypes)
    ruta.insert(INSERT,file_selected)
    Str_file_selected=str(file_selected.name)


    with open("direccion.txt") as archivo:
        for linea in archivo:
            if len(linea)>1:
                print('tiene info')
            else:
                with open("direccion.txt", "a") as f:
                    f.write(Str_file_selected)

    bookOneDrive=file_selected.name
    book =openpyxl.load_workbook(bookOneDrive,data_only=True)
    hoja=book.active
    hoja.title = "DB Excel"
    user=hoja['A2':'A100']
    password=hoja['C2':'C100']
    usernames =[]
    psw =[]
    print(bookOneDrive)
    print(file_selected.name)
    mystr.set(file_selected.name)

    for fila in user:
        info=([celda.value for celda in fila])

        string=' '.join(map(str,info))
        if string =="None":
            string="0"
        if len(string)>1:
            usernames +=[string]
            print(usernames)


    def logIn():
        print(bookOneDrive)
        global usuario
        global count
        global cajaTexto2
        global enviar
        global fila2
        count = count + 1
        text=cajaTexto.get()

        if text=="":
            print('escribe')
            usuario["text"]='Debes poner tu usuario'
        else:
            if boton["text"]=="Cerrar Sesión":
                boton["text"]="Iniciar Sesión"
                cajaTexto2.destroy()
                enviar.destroy()
            else:
                boton["text"]="Cerrar Sesión"

            if boton["text"]=="Cerrar Sesión":
                if usernames.index(text)>=0:
                    user_position=usernames.index(text)+2
                    fila2=str(user_position)
                    user_text=hoja[f'D{fila2}': f'D{fila2}']
                    for info_fila in user_text:
                        info_fila2=([celda2.value for celda2 in info_fila])
                        info_fila2_string=' '.join(map(str,info_fila2))
                        print(info_fila2_string)
                    user_position_table=f"D{user_position}"
                    print(user_position,"\n",user_position_table)

                    cajaTexto2=tk.Text()
                    cajaTexto2.insert(INSERT,info_fila2_string)
                    cajaTexto2.pack()
                    ruta.destroy()

                    def send():
                        text2=cajaTexto2.get("1.0", "end-1c")
                        print(text2)
                        hoja[f'D{fila2}']=text2
                        book.save(bookOneDrive)
                        """hoja["D2"] = "pitudo"
                        print((hoja["D2"])["text"])"""
                    enviar=tk.Button(ventana,text="enviar",command=send)
                    enviar.pack()
                print("hola ",count,"\n","introduciste:",text)
                boton["text"]="Cerrar Sesión"
    boton=tkinter.Button(ventana,text="Inicia Sesión",padx=40,command= logIn)
    cajaTexto=tkinter.Entry(ventana,font="Helvetica 10",bg="#D6D6D6",foreground="gray")

    login.pack(side=tkinter.TOP,fill=tkinter.X)
    cajaTexto.pack()
    usuario=tkinter.Label(ventana)
    usuario.pack()
    boton.pack(pady=20)




ruta=tkinter.Entry(ventana,textvariable=mystr,state='disabled')



count = 0

"""
for fila in password:
    info=([celda.value for celda in fila])
    string=' '.join(map(str,info))
    if string =="None":
        string="0"
    if len(string)>2:
        psw +=[string]
#print(psw)
"""


with open("direccion.txt") as archivo:
    for linea in archivo:
        if len(linea)>1:
            print('tiene info')
            def rutaSet():
                root2 = Tk()
                root2.withdraw()
                filetypes2 = (
                    ('Excel files', '*.xlsx'),
                )
                file_selected2 = filedialog.askopenfile(filetypes=filetypes2)
                Str_file_selected2=str(file_selected2.name)
                with open("direccion.txt", "w") as f:
                    f.write('='+Str_file_selected2)
                ventana.refresh_app2()

            rutaReset=tkinter.Button(text="Nueva Dirección",command=rutaSet)
            directionTxt=linea
            bookOneDrive=str(directionTxt)
            characters = "="
            for x in range(len(characters)):
                bookOneDrive = bookOneDrive.replace(characters[x],"")
            print(bookOneDrive)
            file_selected=bookOneDrive
            book =openpyxl.load_workbook(bookOneDrive,data_only=True)
            hoja=book.active
            hoja.title = "DB Excel"
            user=hoja['A2':'A100']
            password=hoja['C2':'C100']
            usernames =[]
            psw =[]
            print(bookOneDrive)
            print(file_selected)
            mystr.set(file_selected)

            for fila in user:
                info=([celda.value for celda in fila])

                string=' '.join(map(str,info))
                if string =="None":
                    string="0"
                if len(string)>1:
                    usernames +=[string]
                    print(usernames)
            def logIn():
                print(bookOneDrive)
                global usuario
                global count
                global cajaTexto2
                global enviar
                global fila2
                count = count + 1
                text=cajaTexto.get()

                if text=="":
                    print('escribe')
                    usuario["text"]='Debes poner tu usuario'
                else:
                    if boton["text"]=="Cerrar Sesión":
                        boton["text"]="Iniciar Sesión"
                        cajaTexto2.destroy()
                        enviar.destroy()
                    else:
                        boton["text"]="Cerrar Sesión"

                    if boton["text"]=="Cerrar Sesión":
                        if usernames.index(text)>=0:
                            user_position=usernames.index(text)+2
                            fila2=str(user_position)
                            user_text=hoja[f'D{fila2}': f'D{fila2}']
                            for info_fila in user_text:
                                info_fila2=([celda2.value for celda2 in info_fila])
                                info_fila2_string=' '.join(map(str,info_fila2))
                                print(info_fila2_string)
                            user_position_table=f"D{user_position}"
                            print(user_position,"\n",user_position_table)

                            cajaTexto2=tk.Text()
                            cajaTexto2.insert(INSERT,info_fila2_string)
                            cajaTexto2.pack()
                            rutaReset.destroy()
                            def send():
                                text2=cajaTexto2.get("1.0", "end-1c")
                                print(text2)
                                hoja[f'D{fila2}']=text2
                                book.save(bookOneDrive)
                                """hoja["D2"] = "pitudo"
                                print((hoja["D2"])["text"])"""
                            enviar=tk.Button(ventana,text="enviar",command=send)
                            enviar.pack()
                        print("hola ",count,"\n","introduciste:",text)
                        boton["text"]="Cerrar Sesión"
            boton=tkinter.Button(ventana,text="Inicia Sesión",padx=40,command= logIn)
            cajaTexto=tkinter.Entry(ventana,font="Helvetica 10",bg="#D6D6D6",foreground="gray")
            etiqueta.pack(side=tkinter.TOP,fill=tkinter.X)
            login.pack(side=tkinter.TOP,fill=tkinter.X)
            cajaTexto.pack()
            usuario=tkinter.Label(ventana)
            usuario.pack()

            boton.pack(pady=20)
            rutaReset.pack()
        else:
            print('no tiene info')
            ruta2=tkinter.Button(text="seleccionar",command=seleccionar)
            ruta2.pack()

ruta.pack()
ventana.mainloop()

import tkinter as tk
import openpyxl
ventana=tk.Tk()
ventana.geometry('500x700')
ventana.title('Hotel Apaztle')
ventana.iconbitmap('hotel.ico')
book=openpyxl.load_workbook('main.xlsx')
hoja=book.active
celdas=hoja['A2':'B100']
HaT={}
Ti={}
H=hoja['A3':'A29']
T=hoja['A35':'A60']
TP=hoja['B35':'B100']
PH=hoja['B3':'B28']
PHO=hoja['C3':'C28']
E=hoja['A65':'A100']
Habitaciones=[]
Productos=[]
PrecioT=[]
PrecioH=[]
Empleados=[]
Em={}
HabitacionesOC=[]
HabitacionesOC2={}

img=tk.PhotoImage(file='Hotel.png')
title=tk.Label(ventana,text="Hotel Apaztle",bg="#5B9AFF",font="none 12 bold").pack(side=tk.TOP,fill=tk.X)
username=tk.Label(ventana,text="Ingresa tu nombre")
username.pack()
entryBox = tk.Entry(ventana, width=60)

Pe={}

def other():
    global ventana3
    global otroPN
    global otroPP
    ventana3=tk.Tk()
    ventana3.geometry('500x700')
    ventana3.title('Hotel Apaztle')
    ventana3.iconbitmap('hotel.ico')
    title=tk.Label(ventana3,text="Hotel Apaztle (TIENDA/OTRO PRODUCTO)",bg="#5B9AFF",font="none 12 bold").pack(side=tk.TOP,fill=tk.X)
    otroPNL=tk.Label(ventana3,text="Nombre")
    otroPN=tk.Entry(ventana3)
    otroPPT=tk.Label(ventana3,text="Precio")
    otroPP=tk.Entry(ventana3)
    otroPB=tk.Button(ventana3,text="Enviar",command=otroPE)
    otroPNL.pack()
    otroPN.pack()
    otroPPT.pack()
    otroPP.pack()
    otroPB.pack()
#----------------------------------Parte de la Tienda----------------------------------------------------------
def otroPE():
    otroP={}
    otroP[otroPN.get()]=otroPP.get()
    Tuser=f"D{user_position}"
    TPuser=f"E{user_position}"
    TuserExc=hoja[Tuser].value
    TPuserExc=hoja[TPuser].value
    for i in otroP:
        hoja[Tuser]=f"{str(i)+' $'+otroP.get(i)+'|'+TuserExc}"
        hoja[TPuser]=int(otroP.get(i))+TPuserExc
        book.save('main.xlsx')
        Av=tk.Label(ventana3,text=f"La cuenta es de {otroP.get(i)}").pack()
        Av2=tk.Label(ventana3,text="Información guardada exitosamente").pack()


def Tie():
    ventana.destroy()
    global ventana2
    ventana2=tk.Tk()
    ventana2.geometry('500x700')
    ventana2.title('proyecto python')
    ventana2.iconbitmap('hotel.ico')
    title=tk.Label(ventana2,text="Hotel Apaztle (TIENDA)",bg="#5B9AFF",font="none 12 bold").pack(side=tk.TOP,fill=tk.X)
    otro=tk.Button(ventana2,text="Otro producto",command=other).pack()
    for fila in T:
        for celda in fila:
            if celda.value!=None:
                Productos.append(celda.value)
    for fila in TP:
        for celda in fila:
            if celda.value!=None:
                PrecioT.append(celda.value)
    for i in range(len(Productos)):
        Ti[Productos[i]]=PrecioT[i]

    global PP2
    global PP
    PP=[]
    PP2={}
    Cuenta=0
    VCuenta2=[]

    for i in range(len(Ti.keys())):
        Pr=tk.Label(ventana2,text=f"{Productos[i]}")
        Pr.pack()
        Pe[Productos[i]]=tk.Entry(ventana2)
        Pe[Productos[i]].pack()
    PeB=tk.Button(ventana2,text="Enviar",command=PE).pack()
    ventana2.mainloop()
#------------------------------Parte de Habitaciones------------------------------------------------------------

def Ha():
    global HabitacionesCO
    global HabitacionesCO2
    HabitacionesCO=[]
    HabitacionesCO2={}
    HabitacionesCO3=[]
    for fila in H:
        for celda in fila:
            if celda.value!=None:
                Habitaciones.append(celda.value)
    for fila in H:
        for celda in fila:
            if celda.value!=None:
                HabitacionesCO.append(celda.value)
    for fila in PH:
        for celda in fila:
            if celda.value!=None:
                PrecioH.append(celda.value)
    for i in range(len(Habitaciones)):
        HaT[Habitaciones[i]]=PrecioH[i]
    for fila in PHO:
        for celda2 in fila:
            HabitacionesCO3.append(celda2.value)
    for i in range(len(HabitacionesCO3)):
        HabitacionesCO2[HabitacionesCO[i]]=HabitacionesCO3[i]
    print(HabitacionesCO2)

                
                
    
    ventana.destroy()
    global ventana2
    ventana2=tk.Tk()
    ventana2.geometry('500x700')
    ventana2.title('proyecto python')
    ventana2.iconbitmap('hotel.ico')
    title=tk.Label(ventana2,text="Hotel Apaztle (Habitaciones)",bg="#5B9AFF",font="none 12 bold").pack(side=tk.TOP,fill=tk.X)
    HnL=tk.Label(ventana2,text="Ingrese el número de la habitación").pack()

    global HN
    HN=tk.Entry(ventana2)
    HN.pack()
    HNB=tk.Button(ventana2,text="enviar",command=HBNC).pack()








def HBNC():
    NH=HN.get()
    if int(NH) in Habitaciones:
        Oc=tk.Label(ventana2,text=f"REGISTRO EXITOSO").pack()
        Tuser=f"B{user_position}"
        TPuser=f"C{user_position}"
        TuserExc=hoja[Tuser].value
        TPuserExc=hoja[TPuser].value
        TPOC=HabitacionesCO2.get(int(NH))
        hoja[Tuser]=NH+'| '+TuserExc
        for i in HaT:
            if int(NH)==int(i):
                hoja[TPuser]=int(HaT.get(i))+int(TPuserExc)
        book.save('main.xlsx')
    else:
        print('habitación invalida')
    """
    
    
    
    
    NH=HN.get()
    for fila in H:
        for celda in fila:
            if celda.value!=None:
                Habitaciones.append(celda.value)
    for fila in PH:
        for celda in fila:
            if celda.value!=None:
                PrecioH.append(celda.value)
    for i in range(len(Habitaciones)):
        HaT[Habitaciones[i]]=PrecioH[i]
    if int(NH) not in Habitaciones:
        Oc=tk.Label(ventana2,text=f"La habitación {NH} es invalida").pack()
    else:
        HabitacionesCO=[]
        HabitacionesCO2={}
        for fila in PHO:
            for celda in fila:
                if celda.value!=None:
                    HabitacionesOC.append(celda.value)
                    HabitacionesCO.append(celda.coordinate)
    for a in range(len(Habitaciones)):
        print(a)
        print(len(Habitaciones))
        HabitacionesOC2[Habitaciones[a]]=HabitacionesOC[a]
        HabitacionesCO2[Habitaciones[a]]=HabitacionesCO[a]

    Ocupada=HabitacionesOC2.get(int(NH))
    print(Ocupada)
    if Ocupada>0:
        Oc=tk.Label(ventana2,text=f"FALLO EN EL REGISTRO La habitación {NH} esta ocupada").pack()
    else:
        print()
        Oc=tk.Label(ventana2,text=f"REGISTRO EXITOSO").pack()
        Oc2=tk.Label(ventana2,text=f"La habitación {NH} ahora esta ocupada").pack()
        Tuser=f"B{user_position}"
        TPuser=f"C{user_position}"
        TuserExc=hoja[Tuser].value
        TPuserExc=hoja[TPuser].value
        TPOC=HabitacionesCO2.get(int(NH))
        hoja[TPOC]=1
        hoja[Tuser]=NH+'| '+TuserExc
        for i in HaT:
            if int(NH)==int(i):
                hoja[TPuser]=int(HaT.get(i))+int(TPuserExc)
        book.save('main.xlsx')





"""












#-------------------------------LogIn y verificación de usuario------------------------------------------------
def logIn():
    User=cajaTexto.get()
    for fila in E:
        for celda in fila:
            if celda.value!=None:
                Empleados.append(celda.value)
                Em[celda.value]=celda.coordinate
    if User not in Empleados:
        Usern=tk.Label(ventana,text=f"usuario {User} invalido").pack()
        print('usuario invalido')
    else:
        Usern=tk.Label(ventana,text=f"Bienvenido {User}").pack()
        cajaTexto.destroy()
        send.destroy()
        username.destroy()
        userP=Em.get(User)
        global user_position
        user_position=''
        for i in userP:
            if i !='A':
                user_position+=i
        subt=tk.Label(ventana,text="Elija una de las opciones",font="none 20 bold").pack()
        op1=tk.Button(ventana,text="Habitaciones",command=Ha,font="none 12").place(relx=0.1,rely=0.3)
        op2=tk.Button(ventana,text="Tienda",command=Tie,font="none 12").place(relx=0.8,rely=0.3)


#------------------------SUMA DE PRODUCTOS Y CALCULO DE COSTOS------------------------------------
def PE():
    PC={}
    PCA=[]
    SumaCuenta = 0
    for i in range(len(Ti.keys())):
        Cantidad=Pe.get(Productos[i]).get()
        P=Ti.get(Productos[i])
        if Cantidad=='':
            Cantidad=0
        C=int(Cantidad)*int(P)
        if int(Cantidad)>0:
            PC[Productos[i]]=Cantidad
            PCA.append(C)
    Total=0
    for i in PCA:
        Total = Total+i
    Tuser = f"D{user_position}"
    TPuser = f"E{user_position}"
    TuserExc = hoja[Tuser].value
    TPuserExc = hoja[TPuser].value
    if str(PC)!='{}':
        hoja[Tuser]=str(PC)+TuserExc
        hoja[TPuser]=Total+TPuserExc
        book.save('main.xlsx')
        Av = tk.Label(ventana2,text=f"La cuenta es de {Total}").pack()
        Av2 = tk.Label(ventana2,text="Información guardada exitosamente").pack()

cajaTexto = tk.Entry(ventana,font="Helvetica 10",bg="#D6D6D6",foreground="gray")
cajaTexto.pack()
send = tk.Button(ventana,text="Iniciar",command=logIn)
send.pack()
ventana.mainloop()

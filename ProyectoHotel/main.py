import openpyxl
from colorama import init,Fore,Back,Style
init()
book=openpyxl.load_workbook('main.xlsx')
hoja=book.active
celdas=hoja['A2':'B100']
Ha={}
Ti={}
H=hoja['A3':'A29']
T=hoja['A35':'A60']
TP=hoja['B35':'B100']
PH=hoja['B3':'B28']
E=hoja['A65':'A100']
Habitaciones=[]
Productos=[]
PrecioT=[]
PrecioH=[]
Empleados=[]
Em={}
for fila in H:
    for celda in fila:
        if celda.value!=None:
            Habitaciones.append(celda.value)
for fila in PH:
    for celda in fila:
        if celda.value!=None:
            PrecioH.append(celda.value)
for fila in T:
    for celda in fila:
        if celda.value!=None:
            Productos.append(celda.value)
for fila in TP:
    for celda in fila:
        if celda.value!=None:
            PrecioT.append(celda.value)

for i in range(len(Habitaciones)):
    Ha[Habitaciones[i]]=PrecioH[i]
for i in range(len(Productos)):
    Ti[Productos[i]]=PrecioT[i]
for fila in E:
    for celda in fila:
        if celda.value!=None:
            Empleados.append(celda.value)
            Em[celda.value]=celda.coordinate

Title='Hotel Apaztle'

print(Fore.RED+Title.center(50, "="))
print(Fore.RESET+'Cual es tu nombre?')
User=input()
while User not in Empleados:
    print(Fore.YELLOW+'Usuario invalido')
    User=input(Fore.RESET+'Cual es tu nombre?')
print(Fore.BLUE+f'Bienvenid@ {User}')
userP=Em.get(User)
user_position=''
for i in userP:
    if i !='A':
        user_position+=i
print(user_position)

for i in range(50):
    print('-',end="")
print(Fore.RESET+'\nHabitacion [H]  Tienda [T]\n')
op=input()

while op.lower()!="h" and op.lower()!="t":
    print(Fore.YELLOW+'invalido')
    op=input(Fore.RESET+'\nHabitacion [H]  Tienda [T]\n')



#-----------------------------Habitaciones
if op.lower() =="h":
    print('Habitaciones')
    print(Habitaciones)
    print(Ha)
    Hu=int(input('ingrese el número de la habitación: '))
    print(Fore.RESET+f'la habitación elegida es '+Fore.YELLOW+f'{Hu}'+Fore.RESET+', desea continuar [S]=Sí [N]=No\n')
    Op2=input()
    while Op2.lower()!="s" and Op2.lower()!="n":
        print(Fore.YELLOW+'invalido')
        print(Fore.RESET+f'la habitación elegida es '+Fore.YELLOW+f'{Hu}'+Fore.RESET+', desea continuar [S]=Sí [N]=No\n')
        Op2=input()
    if Op2=='s':
        if Hu in Habitaciones:
            print(f'La habitación {Hu} ahora esta opcupada')
            Op5=input('desea agregar otra habitación? [S]=Sí [N]=No')
            while Op5.lower()!="s" and Op5.lower()!="n":
                Op5=input('desea agregar otra habitación? [S]=Sí [N]=No')
            if Op5=='s':
                print('agrega otra habitación')
            else:
                print('noob')
        else:
            print(f'La habitación '+Fore.YELLOW+f'{Hu}'+Fore.RESET+' no se encuentra, verifique su numeración')
    else:
        print('noob')

#-----------------------------TIENDA
else:
    PP=[]
    PP2={}
    Cuenta=0
    VCuenta2=[]
    print('Tienda')
    print(Productos)
    print(Ti)
    NP=input('Cuantos productos se vendieron?')
    RE=input('Se repiten algunos productos? [S]=Sí [N]=No ')
    while RE.lower()!="s" and RE.lower()!="n":
        RE=input('Se repiten algunos productos? [S]=Sí [N]=No ')
    if RE=='s':
        P=input('Ingrese el nombre del producto repetido: ')
        if P not in Productos:
            print('prodcuto invalido')
        else:
            PR=int(input('ingrese el numero de veces que se repite: '))
            PP2[P]=PR
            print(PP2)

    else:
        def ProdInd():
            print(f'la cantidad de productos es '+Fore.RED+f'{NP}'+Fore.RESET+', desea continuar [S]=Sí [N]=No\n')
            Op3=input()
            while Op3.lower()!="s" and Op3.lower()!="n":
                print(Fore.YELLOW+'invalido')
                print(f'la cantidad de productos es '+Fore.RED+f'{NP}'+Fore.RESET+', desea continuar [S]=Sí [N]=No\n')
                Op3=input()
            if Op3=='s':
                for i in range(int(NP)):
                    PU=input(f'Ingrese el nombre del producto {i+1}: ')
                    if PU not in Productos:
                        print(Fore.YELLOW+f'Producto {PU} invalido ')
                        PU=input(Fore.RESET+f'Ingrese el nombre del producto {i+1}: ')
                        PP.append(PU)
                    else:
                        PP.append(PU)
                for item in PP:
                    if item not in PP2.keys():
                        PP2[item]=1
                    else:
                        PP2[item]+=1
                for i in PP2:
                    Cuenta=PP2.get(i)
                    VCuenta=Ti.get(i)*Cuenta
                    VCuenta2.append(VCuenta)
                print(f'los productos son '+'\033[3;41m'+f'{PP2}'+'\033[0;0m'+', desea continuar [S]=Sí [N]=No\n')
                Op4=input()
                while Op4.lower()!="s" and Op4.lower()!="n":
                    print(Fore.YELLOW+'invalido')
                    print(f'los productos son '+'\033[3;41m'+f'{PP2}'+'\033[0;0m'+', desea continuar [S]=Sí [N]=No\n')
                    Op4=input()
                if Op4=='s':
                    SumaCuenta = 0
                    for suma in VCuenta2:
                        SumaCuenta += suma
                    print(f"La cuenta es de {SumaCuenta}")
                    Tuser=f"E{user_position}"
                    TPuser=f"D{user_position}"
                    print(Tuser)
                    TuserExc=hoja[Tuser].value
                    TPuserExc=hoja[TPuser].value
                    TuserTotal=SumaCuenta+TuserExc
                    TPuserTotal=TPuserExc+str(PP2)
                    hoja[Tuser]=TuserTotal
                    hoja[TPuser]=TPuserTotal
                    book.save('main.xlsx')
                    print(f"has vendido {TuserTotal}")
                else:
                    print('noob')
            else:
                print('noob')
        ProdInd()
k=input("Da ENTER para salir")
book.save('main.xlsx')

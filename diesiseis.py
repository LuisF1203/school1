#tamaño a y b
#tamaños 1 y 2
#si es de tipo a se le cargan 20 si es 1, si es 2 se le cargan 30
#si es de tipo b se le restan 30 si es 1, si es 2 se le restan 50

tipo=str(input('ingrese el tipo de uva "A" o "B": '))
precio=eval(input('introduce el precio por uva: '))
tamaño=eval(input('introduce el tamaño 1 o 2: '))
cantidad=int(input('introduce la cantidad de uvas '))
if(str(tipo)=="A" or str(tipo)=="a"):

    if(tamaño==1):
        precio+=precio+0.20;
        ganancia=precio*cantidad
        print(f'elegiste el tamaño 1\nEl precio del producto será:{precio}\nLa ganancia será de {ganancia}')
    if(tamaño==2):
        precio+=precio-0.30;
        ganancia=precio*cantidad
        print(f'elegiste el tamaño 1\nEl precio del producto será:{precio}\nLa ganancia será de {ganancia}')

    else:
        print('tipo de tamaño no encontrado')
        exit()
    print('es de tipo A, el precio por uva es de:',precio)
if(str(tipo)=="B" or str(tipo)=="b"):
    print('es de tipo B, el precio por uva es de:',precio)
else:
    print('tipo de uva no encontrado')


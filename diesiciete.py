#ejercicio 6
#claves (1,2,3,4,5 y 6 )
#se requiere un calcular los precios de venta
#costo de producción= materia prima + mano de obra+gastos de fabricación
#precio de venta=costo de producción+45% de costo de producción
#costo de mano de obra=
# claves (3 o 4)=75%
# claves (1 o 5)=80%
# claves (2 o 6)=85%
#gasto de fabricación sobre el costo de la materia prima=
# 30%=claves (2 o 5 )
# 35%=claves (3 o 6)
# 28%=claves (1 o 4)
import sys

clave=eval(input('introduce la clave entre los numeros 1 al 5\n'))
material=int(input('introduce el costo de la materia prima\n'))


""" COSTO DE MANO DE OBRA  """
if clave>0 and clave<16:
    print(f'perfecto [el valor {clave}, cumple con las condiciones dadas]')
    #costoP=material+manoObra+gastosF
    #inicio del programa
    costoO=material
    if clave==3 or clave==4:
        if clave==1 or clave==4:
            costoF=costoO*0.28
            print(f'{clave},{costoF}')
        if clave==3 or clave==6:
            costoF=costoO*0.35
            print(f'{clave},{costoF}')
        costoO=costoO*0.75
        print(f'{clave},{costoO}')
    if clave==1 or clave==5:
        if clave==1 or clave==4:
            costoF=costoO*0.28
            print(f'{clave},{costoF}')
        if clave==2 or clave==5:
            costoF=costoO*0.30
            print(f'{clave},{costoF}')
        costoO=costoO*0.80
        print(f'{clave},{costoO}')
    else:
        if clave==2 or clave==5:
            costoF=costoO*0.30
            print(f'{clave},{costoF}')
        if clave==3 or clave==6:
            costoF=costoO*0.35
            print(f'{clave},{costoF}')
        costoO=costoO*0.85
        print(f'{clave},{costoO}')

else:
    print(f'ingrese otros valores [el valor {clave}, no cumple con las condiciones dadas]')
    sys.exit()



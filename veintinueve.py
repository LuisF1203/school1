"""Cadena de atoservicion cuenta con sucursalen en C ciudades """

Ciudades=int(input('¿En cuantas ciudades se encuentra?\n'))
ValVentas=0
ValVentas2=0
ValCiudad2=0
ValCiudad=0
ValTienda=[]
ValEmpleados=[]
ValTienda2=[]
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

for i in range(Ciudades):
    Tiendas=int(input(f'{bcolors.RESET}Cuantas tiendas hay en la ciudad {i+1}\n'))
    for c in range(Tiendas):
        Empleados=int(input(f'{bcolors.RESET}Ingresa la cantidad de empleados en la tienda {c+1}: '))
        for e in range(Empleados):
            Ventas=eval(input(f'{bcolors.RESET}Ingresa la cantidad de ventas para el empleado {e+1}: '))
            ValVentas=ValVentas+Ventas
            ValVentas2=ValVentas2+Ventas
            ValTienda.append(Ventas)
            ValEmpleados.append(Ventas)
            ValCiudad=ValCiudad+Ventas
            print(f'{bcolors.RED}En la ciudad {e+1} hay {Empleados} empleados y se vendió {ValCiudad}')
        ValTienda2.append(ValCiudad)
        ValCiudad=0
        ValVentas=0
for g in range(1,41,1):
    print("-",end="")
print(f'\n{bcolors.YELLOW}La cadena recaudo en un dia:{ValVentas2},en cada tienda se vendió {ValTienda2}')
for e2 in range(len(ValEmpleados)):
    print(f"El empleado {e2+1} vendió {ValEmpleados[e2]}")

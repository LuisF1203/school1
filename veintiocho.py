"""print('\t\t\tTABLA DE MULTIPLICAR')
print('\t',end="")
for i in range(1,10,1):
    print(i,end="\t")
print("\n")
for i in range(1,41,1):
    print("-",end="")
print("\n")
for i in range(1,10,1):
    print(i,"|",end=" ")
    for j in range(1,10,1):
        print(i*j,end="\t")
    print('\n')
   """
"""
print('\t\t TABLA DE MULTIPLICAR')
print('\t',end="")
for i in range(1,10,1):
    print(i,end="\t")
print("\n")
for i in range(1,41,1):
    print("-",end="")
for i in range(1,10,1):
    print("\n ",end="")
    for j in range(1,11,1):
        print(j*i,end="\t ")
"""
#una empresa les paga a asus empleados con base en las hras trabajadas en la semna , para esto, se registra los días que laboró y las horas de cada día
trabajadores=int(input('Ingrese la cantidad de trabajadores: \n'))
pagohora=eval(input('Ingrese el salario por hora\n'))
nomina=0
for i in range(1,trabajadores+1,1):
    dias=int(input(f'Ingrese la cantidad de días laborados para el empleado {i}\n'))
    for j in range(1,dias+1,1):
        horas=int(input(f'cuantas horas trabajo el empleado {i} en el día {j}?\n'))
        sueldo=horas*pagohora
        nomina=nomina+sueldo
print(f'La nomina final es de: ${nomina} para {trabajadores} empleados')

"""numero=eval(input('cuantos numeros quieres?\n'))
a=0
b=1
for i in range(numero):
    print(a, end=' ')
    a, b = b, a + b

"""

numero=eval(input('Cual numero quieres buscar?\n'))
a=0
b=1
valor=""
numeros=[]
for i in range(0,numero):
    if i==0 or i==1:
        numeros.append(1)
    else:
        numeros.append(numeros[-2]+numeros[-1])
for i in (numeros):
    if numero==i:
        valor="si"

if valor=="si":
    print(f'El numero {numero} se encuentra en la serie')
else:
    print(f'El numero {numero} no se encuentra en la serie')

"""
for i in range(numero):
    a, b = b, a + b
    if numero==a:
        valor="Si"
if valor=="Si":
    print(f'\nEl numero {numero} se encuentra')
else:
    print(f"\n El numero {numero} no se encuentra")
"""
"""   
num=20
numeros=[]
for i in range(0,num):
    if i==0 or i==1:
        numeros.append(1)
    else:
        numeros.append(numeros[-2]+numeros[-1])
print(numeros)
"""

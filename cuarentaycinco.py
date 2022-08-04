"""
Archivos Externos

manejador=open('ejemplo3.txt', 'r')
#contenido=manejador.read(10)
#manejador.seek(10)#mueve el puntero hacia donde lo indiquew
#contenido=manejador.read()
#linea=manejador.readline()
list=manejador.readlines()
print(list

manejador=open('ejemplo3.txt', 'r')
linea=manejador.readline()
posicion=manejador.tell()
print(posicion)

manejador=open('ejemplo1.txt','w')
manejador.write('hola')

lista=[]
num=eval(input('Cuantos nombres quieres ne la lista'))
for i in range(num):
    nombre=input('ingresa tu numbre')
    lista.append(nombre)
manejador=open('ejemplo2.txt','w+')
manejador.writelines(lista)
manejador.seek(0)
print(manejador.read())
"""
lista=[]
num=eval(input('Cuantos nombres quieres ne la lista'))
for i in range(num):
    nombre=input('ingresa tu numbre')
    lista.append(nombre)
manejador=open('ejemplo2.txt','w+')
for i in range(num):
    manejador.write(lista[i])
    manejador.write(' ')

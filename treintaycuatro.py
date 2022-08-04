"""
Agregar elementos a ala lista (concatenando listas )
Ejemplo
lista[1,2,3,4,5]
lista=lista+[6] agregar elementos
lista.append(elemento)

"""
Lista1=[1,2,3,4,8,0,1]
print(Lista1)
numero=eval(input('dame un numero'))
Lista1.append(numero)
pos=eval(input('dame una posición'))
Lista1.insert(pos,numero)
Lista1=Lista1+[6]
print(Lista1)
Lista1.pop(2)
print(Lista1)
del(Lista1[1:3:1])
print(Lista1)
Lista1.clear()
print(Lista1)
#del(lista[start:stop:step]) sirve para eliminar revanadas de una lista

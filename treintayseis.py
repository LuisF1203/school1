"""
Encontrar elementos repetidos en una lista

"""

lista1=[1,2,1,1,3,4,4,4,5,6,7,8,9,0]
x=lista1.count(4)
print(f"el numero 4 se repite {x} veces")


"""

Función index

busca un elemento en la lista y regresa la poición en la que se encuentra

"""
x=lista1.index(4)
print(f"El numero 4 se encuentra en la posición {x}")
lista1.pop(x)
print(lista1)

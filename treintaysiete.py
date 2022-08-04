"""
ORDENAMIENTOS

ORDENAMIENTO DE BURBUJA

5 7 2 3 9 23 54 7 21 3
"""
def ordenar(lista,numero):
    for i in range(0,numero-1,1):
        for j in range(i+1,numero,1):
            if lista[i]>lista[j]:
                temp=lista[i]
                lista[i]=lista[j]
                lista[j]=temp
    return lista
def crearlista(numero):
    lista1=[]
    for i in range(numero):
        print(f'Dime el numero {i+1}',end="")
        num=eval(input())
        lista1.append(num)
    return lista1
numero=int(input('Cuantos numeros quieres de la lista?'))
while numero<1:
    print("Error, el numeor de elementos no puede ser menor que 1 ")
    numero= int(input('cuantos numeros queres en la lista: '))
lista=crearlista(numero)
print('la lista original: ',lista)

#lista=ordenar(lista,numero)
print('la lista ordenada: ',ordenar(lista,numero))

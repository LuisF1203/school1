def crearlista(numero):
    lista1=[]
    for i in range(numero):
        print(f'Dime la palabra numero {i+1}',end="")
        palabra=input()
        lista1.append(palabra)
    return lista1
numero=int(input('Cuantos numeros quieres de la lista?'))
while numero<1:
    print("Error, el numeor de elementos no puede ser menor que 1 ")
    numero= int(input('cuantos numeros queres en la lista: '))
lista=crearlista(numero)

palabra=input('¿Qué palabra quieres eliminar?')

if palabra not in lista:
    print('no esta')
else:
    for i in range(len(lista)-1,-1,-1):
        if palabra == lista[i]:
            lista.pop(i)
print(lista)

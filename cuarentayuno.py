def crearLista(numero):
    lista1=[]
    for i in range(numero):
        print(f'dame la palabra número {i+1}:',end="")
        palabra=input()
        lista1.append(palabra)
    return lista1
numero1=int(input('Cuantas palabras quieres en la lista: '))
lista1=crearLista(numero1)
print('lista original',lista1)
for i in range(len(lista1)-1,-1,-1):
    for j in range(i-1,-1,-1):
        if lista1[i]==lista1[j]:
            lista1.pop(i)
print("lista sin repetidos: ",lista1)

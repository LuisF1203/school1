def crearlista(numero):
    lista1=[]
    for i in range(numero):
        print(f'Dime la palabra numero {i+1}',end="")
        palabra=input()
        lista1.append(palabra)
    return lista1


numero=eval(input('cuantas palabras quieres?'))

while numero<1:
    print("Error, el numeor de elementos no puede ser menor que 1 ")
    numero= int(input('Cuantas palabras quieres? '))
lista1=crearlista(numero)
numero=int(input('cuantas palabras quieres?'))

while numero<1:
    print("Error, el numeor de elementos no puede ser menor que 1 ")
    numero= int(input('Cuantas palabras quieres? '))
lista2=crearlista(numero)
print(lista1)
for i in range(0,len(lista2),1):
    for j in range(len(lista1)-1,-1,-1):
        if lista2[i]==lista1[j]:
            lista1.pop(j)
print(lista1)

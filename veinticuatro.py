#programa para generar n numero de la suseción fibonacci
numero=eval(input('cuantos numeros quieres?'))
numeros=[]
for i in range(numero):
    numeros.append(i)
    print(numeros[i]+numeros[i])

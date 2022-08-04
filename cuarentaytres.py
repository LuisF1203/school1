"""
Escribe un programa que lea una cadena y devuelva un diccionatio con la cantidad de apariciones de cada caráter en la cadena
"""

palabra=str(input('escribe la palabra'))
print(palabra)
diccionario={}
for i in range(len(palabra)):
    print(palabra[i])
    if palabra[i] not in diccionario:
        diccionario[palabra[i]]=1
    else:
        diccionario[palabra[i]]+=1
print(diccionario)
for llave,valor in diccionario.items():
    print(f'la letra {llave}, está {valor} veces')

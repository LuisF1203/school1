"""
Escriba un programa que permita crear dos listas de palabras y que, a
continuación, escriba las siguientes listas (en las que no debe haber
repeticiones):
• Lista de palabras que aparecen en las dos listas.
• Lista de palabras que aparecen en la primera lista, pero no en la segunda.
• Lista de palabras que aparecen en la segunda lista, pero no en la primera.
• Lista de palabras que aparecen en ambas listas.
•Nota: Para evitar las repeticiones, el programa deberá empezar
eliminando los elementos repetidos en cada lista.
"""
data = []
data2 = []
final = []
final2 = []
ambas = []
primera = []
segunda = []
P=eval(input('¿Cuantas palabras quieres para la primera lista? '))
for i in range(P):
    palabra=input(f'Ingrese la palabra {i+1}: ')
    data.append(palabra)
    for w in data:
        if w not in final:
            final.append(w)
print(final)
P2=eval(input('¿Cuantas palabras quieres para la segunda lista? '))
for j in range(P2):
    palabra2=input(f'Ingrese la palabra {j+1}: ')
    data2.append(palabra2)
    for w2 in data2:
        if w2 not in final2:
            final2.append(w2)
for i in final:
    if i in final2:
        ambas.append(i)
    else:
        primera.append(i)
for i in final2:
    if i not in final:
        segunda.append(i)
print(chr(27)+"[1;34m"+f'LISTA DE LAS DOS: {final,final2}\n'
      +chr(27)+"[1;33m"+f'PALABRAS QUE APARECEN EN LA PRIMERA,PERO NO EN LA SEGUNDA: {primera}\n'
      +chr(27)+"[1;32m"+f'PALABRAS QUE APARECEN EN LA SEGUNDA,PERO NO EN LA PRIMERA : {segunda}\n'
      +chr(27)+"[1;31m"+f'AMBAS LISTAS: {ambas}')

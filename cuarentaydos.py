"""
Diccionario, es un tipo de lista no otdenada en la cual cda elemento estqpa asociado a una llave

las llaves deben de ser únicas

CREANDO DICCIONARIOS



"""

#DICCIONARIO VACIO
diccionario1={}
diccionario1=dict()
diccionario1["a"]=100
diccionario1["b"]=200
print(diccionario1)
x=len(diccionario1)
print(f'Mi diccionario tiene {x} elementos')
del(diccionario1['a'])
print(diccionario1)
diccionario1[70]="París"
diccionario1["Estado"]=32
diccionario1["Ciudad"]="Guadalajara"
print(diccionario1.keys())
print(diccionario1.values())
print(diccionario1.get(70))
print(diccionario1.popitem())
if 70 in diccionario1:
    print('está')
else:
    print('no está')
if "Municipio" not in diccionario1: #También funciona con array
    print('No está')
else:
    print('está')

a="*"
for i in range(10):
    print(a,end="\n")
    a=a+"\t*"

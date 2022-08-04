"""

Crear un programa donde vamos a declarar un diccionario par guardar los precio de las distintas frutas
"""
frutas={}
num=eval(input('cuantas frutas vendes?'))

for i in range(0,num,1):
    nombre=str(input(f'dame el nombre de la fruta {i+1}'))
    precio=eval(input(f'dame el precio de la fruta {i+1}'))
    frutas[nombre.lower()]=precio
total=0
print(frutas)
opcion="S"
while opcion.lower()=="s":
    fruta=input('que fruta quieres comprar: ')
    if fruta.lower() not in frutas:
        print(f'La fruta {fruta} no se encuentra en nuestro inventario')
    else:
        print(f'La fruta {fruta} tiene un precio de {frutas.get(fruta.lower())}')
        pesos=eval(input(f'Cuantos kilos de {fruta} quieres'))
        subtotal=pesos*frutas[fruta.lower()]
        print(f'la cuenta por {pesos} es de {subtotal}')
        total=total+subtotal
        opcion=input('quires comprar otra fruta   [S]=sí  [N]=No \n')
print(f'El total a pagar es {total} pesos')

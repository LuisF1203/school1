"""Validar datos de entrada

ya sabemos hacer un algoritmo que calcule el precio + IVA  de un producto, dado su precio

¿Y si el usuairo no escribe bien el precio?
(escribe un numero negativo)?

¿Qué tal si le preguntemos?


ESTRUCTURAS REPETITIVAS

"""
print('suseción fibonacci\n')
numero=eval(input('ingresa la cantidad de numeros\n'))
i=0
array=[]
while i<numero:
    array.extend([i+1])
    i=i+1
for i in range(numero):
    fibonacci=array[i]
    numero2=array[-numero]
    print(fibonacci+numero2)


def saludar():
    print('hola')


def suma(a,b):
    c=a+b
    print(f'la suma de {a} + {b} es {c}')
suma(1,2)

a=eval(input('Dame el numero 1: '))
b=eval(input('Dame el numero 2: '))

suma(a,b)

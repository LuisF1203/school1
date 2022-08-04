import math
import sys
opcion=int(input('Elige una opción\n1.-Triangulo\n2.-Circulo\n3.-Cilindro\n'))
if opcion>3 or opcion<=0:
    print(f'numero de opción no valida [{opcion}]')
    sys.exit()
else:
    if opcion==1:
        forma="triangulo"
        print('AREA TRIANGULO\n')
        base=eval(input('introduce la base del triangulo:'))
        altura=eval(input(f'introduce la Altura del {forma}:'))
        area=(base*altura)/2
    elif opcion==2:
        forma="circulo"
        print('AREA DE UN CIRCULO')
        radio=eval(input('ingrese el radio:\n',))
        area=(math.pi*radio)**2
    elif opcion==3:
        forma="cilindro"
        print('AREA DE UN CILINDRO')
        radio=eval(input('ingrese el radio:\n'))
        altura=eval(input(f'introduce la Altura del {forma}:'))
        area=math.pi*radio**2*altura
print(f'El area del {forma} es: {area}')

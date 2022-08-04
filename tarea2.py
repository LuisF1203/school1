ventas=eval(input('introduce el numero de ventas\n'))
if ventas<=500:
    print(f'{ventas} ventas menores a 501')
    print(f'El total de ventas fue:{ventas}')
    exit()
if ventas>1000:
    print(f'{ventas} ventas mayores a 1000')
    print(f'El total de ventas fue:{ventas}')
    exit()
if ventas>500:
    print(f'{ventas} ventas mayores a 500')
    print(f'El total de ventas fue:{ventas}')
    exit()

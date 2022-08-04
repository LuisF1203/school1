cal=eval(input('introduce la calificación\n'))
if cal>=9.5 and cal<=10:
    cal=10
    print('10')
elif cal>=8.5:
    cal=9
elif cal>=7.5:
    cal=8
elif cal>=6.5:
    cal=7
elif cal>=6:
    cal=6
elif cal<6:
    cal=0


if cal<=0:
    print('reprobado')
else:
    print(cal)

